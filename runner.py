from git_details.gitlib import GitDetails

if __name__ == '__main__':
    path = "/home/marcin/projects/myrepo1"

    g = GitDetails(repo_path=path, user_name='Marcin', since_date='2020-05-01')
    g.get_commits(print_details=True)
