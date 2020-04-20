#!/usr/bin/env python

from github import Github
from credentials import token
from sys import argv
import subprocess


def main():
    # checking if all args provided
    if not len(argv) in range(2, 4):
        print("Usage: devpro.py reponame [optional:template]")
        quit()

    # check if second argument provided
    if argv[2]:
        # list of all available Templates
        templates = ["website", "flask"]
        # check if provided argument is in templates list
        if not argv[2].lower() in templates:
            print(f"Template {argv[2]} not available. Available "
                  "Templates: ", end="")
            for item in templates:
                print(f"{item}", end=" ")
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

    # create folders and files depending on second argv
    if argv[2]:
        create_template(argv[2], repo, repo_name)

    # getting the new repo url
    repo_url = repo.git_url

    # cmd for cloning github repo
    cmd_clone = ["git", "clone", repo_url]
    # running the command
    subprocess.run(cmd_clone)

    # create image folder locally, cannot have empty folders on github
    if argv[2] == "website":
        subprocess.run(["mkdir", repo_name + "/img"])


def create_template(temp, repo, repo_name):
    if temp == "website":
        # create files
        repo.create_file("index.html", "init commit", "")
        repo.create_file("css/styles.css", "init commit", "")
        repo.create_file("js/functions.js", "init commit", "")
    elif temp == "flask":
        repo.create_file("application.py", "init commit", "")
        repo.create_file("static/styles.css", "init commit", "")
        repo.create_file("templates/index.html", "init commit", "")


if __name__ == "__main__":
    main()
