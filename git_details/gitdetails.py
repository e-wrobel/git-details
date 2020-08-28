from git_details.gitlib import GitDetails
import argparse

example_usage = 'Example usage: \npython3 git-details.py /home/ubuntu/my_repo "Mr Sparrow" 2020-08-01 --details Y ' \
                '\nOR when running from installed package in native/docker/virtualnenv: ' \
                '\ngit-details /home/ubuntu/my_repo "Mr Sparrow" 2020-08-01 --details Y'


def parse():
    parser = argparse.ArgumentParser(description='Git details for selected user and repository',
                                     epilog=example_usage)
    parser.add_argument('path', type=str,
                        help='path to local repository')
    parser.add_argument('user', type=str,
                        help='Search will be narrowed to the selected user, for example \"Mr Sparrow\"')
    parser.add_argument('since', type=str,
                        help='Search will be narrowed to selected since date, for example: 2020-08-01')
    parser.add_argument('--details', type=str, default='Y',
                        help='To print just commits or whole changes (git show): Y/N')
    arguments = parser.parse_args()

    return arguments


# main() is required by setup.py -> Entrypoints
def main():
    args = parse()

    details = args.details
    details = True if details == 'Y' else False

    g = GitDetails(repo_path=args.path, user_name=args.user, since_date=args.since)
    g.get_commits(print_details=details)


if __name__ == '__main__':
    main()
