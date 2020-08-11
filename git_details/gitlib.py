import json
from subprocess import Popen, PIPE

from git import Repo


class GitDetails(object):
    def __init__(self, repo_path: str, user_name: str, since_date: str):
        """
        :param repo_path: Path to the repository (has to contain .git)
        :param user_name: We will search for commits containing given user name
        :param since_date: We will search since given date in format YYYY-MM-DD
        """

        self.repo_path = repo_path
        self.user_name = user_name
        self.since_date = since_date
        self.total_insertions = 0
        self.total_deletions = 0
        self.total_linet = 0

        self.repo = Repo(path=repo_path)

    def get_commits(self, print_details=False):
        """
        Print all commits basic information for selected repository, username and date.
        If print_details is set to True than detailed information will be printed.

        :param print_details: Stands for printing detailed information for the commits
        """

        commits = self.repo.iter_commits(since=self.since_date, author=self.user_name)

        for commit in commits:
            self.__print_commit_basic_info(commit)
            if print_details:
                self.__print_commit_detailed_info(commit.hexsha, self.repo_path)

        self.__print_total_insertions_deletions()

    def __print_commit_basic_info(self, commit):
        """
        Print basic information for selected commit number.

        :param commit: Commit object
        :type commit: Commit
        """

        print("\nCommit: {}\n{} {} by {} ({})".format(commit.hexsha, str(commit.authored_datetime), commit.summary,
                                                      commit.author.name, commit.author.email))
        files = commit.stats.files
        print(json.dumps(files, sort_keys=True, indent=4))

        for _, file_val in files.items():
            self.total_insertions += file_val['insertions']
            self.total_deletions += file_val['deletions']

    def __print_commit_detailed_info(self, commit, working_dir):
        proc = Popen(['git', 'show', commit],
                     cwd=working_dir,
                     shell=False,
                     stdout=PIPE,
                     stderr=PIPE)

        out, _ = proc.communicate()

        for line in out.decode('utf-8').split('\n'):
            print(line)

    def __print_total_insertions_deletions(self):
        a = any([self.total_deletions, self.total_insertions])
        if a:
            print("\nTotal insertions: {}\nTotal deletions: {}\nDifference: {}".format(self.total_insertions,
                                                                                       self.total_deletions,
                                                                                       abs(
                                                                                           self.total_insertions - self.total_deletions)))
        else:
            print("No commits found for user: {}, since: {}".format(self.user_name, self.since_date))

