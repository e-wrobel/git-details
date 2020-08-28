from setuptools import setup, find_packages
setup(
    name="git-details",
    version="0.1",
    packages=find_packages(),
    author="Mr. Sparrow",
    author_email="marcin.wroblewski@aol.com",
    description="Git-Details allows to check code changes for given developer",
    keywords="git code developer",
    url="https://github.com/e-wrobel/git-details",

    classifiers=[
        "License :: OSI Approved :: Python Software Foundation License"
    ],

    entry_points={
        "console_scripts": [
            'git-details=git_details.gitdetails:main'
        ],
    }
)
