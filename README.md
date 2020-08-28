# Summary:
This repository contains tool for getting git details - mainly details about commits - for selected user, and since given date.
It can be used to show your work progress on selected repository (and also branch).

# Remark:
You need to install git commandline tool.

# How to install:
1. Build package using make_package.sh bash script,

2. Install requirements: pip install -r requirements.txt,

3. Install package: pip install dist/git_details-0.1-py3-none-any.whl.

# How to uninstall:
1. pip uninstall git-details

# How to use it:
Example usage:
 
python3 git-details.py /home/ubuntu/my_repo "Mr Sparrow" 2020-08-01 --details Y

OR when running from installed package in native/docker/virtualnenv:
 
git-details /home/ubuntu/my_repo "Mr Sparrow" 2020-08-01 --details Y

If you want less data (just commits without code changes) use: --details N
