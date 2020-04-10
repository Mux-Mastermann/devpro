#!/usr/bin/env python

from github import Github
from sens import token
from sys import argv
import subprocess


# checking in all args provided
if not len(argv) == 2:
    print("Usage: python devpro [reponame]")
    quit()

# setting new repo name
repo_name = argv[1]

# creating instance of github and of github user
g = Github(token)
user = g.get_user()

# creating new repository
repo = user.create_repo(repo_name)
# checking for error (if repo name already exists for example)
# TODO

# create README
readme = "# " + repo_name
repo.create_file("README.md", "init commit", readme)

# getting the new repo url
repo_url = repo.git_url

# cmd for cloning github repo
cmd_clone = ["git", "clone", repo_url]
# running the command
subprocess.run(cmd_clone)
