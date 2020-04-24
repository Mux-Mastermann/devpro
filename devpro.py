#!/usr/bin/env python

import subprocess
import json
import os

from github import Github
from credentials import token
from sys import argv


def main():
    # getting the location of the script
    script_dir = os.path.dirname(__file__)
    # Definining Keyword for creating and changing boilerplates
    KEYWORD_BOILERPLATE = "boilerplate"
    # Indicates if boilerplate was entered by user
    bool_boilerplate = False

    # checking if all args provided
    if not len(argv) in range(2, 4):
        print("Usage: devpro.py reponame [optional:boilerplate]")
        quit()

    if len(argv) == 3:
        bool_boilerplate = True
        # capturing the entered boilerplate in variable
        boilerplate = argv[2].lower()

        # load boilerplates.json to a dict
        with open(script_dir + "/boilerplates.json", "r") as read_file:
            boilerplates = json.load(read_file)

        # check if the Keyword for CRUD boilerplates was entered
        if boilerplate == KEYWORD_BOILERPLATE:
            # Run a CRUD function for the boilerplate
            CRUD_boilerplates(argv[1], boilerplates)
            quit()
        # check if entered boilerplate exists in boilerplates
        elif boilerplate not in boilerplates.keys():
            print(f"The boilerplate '{boilerplate}' does not exist.\n"
                  "You can create boilerplates with keyword: 'boilerplate'\n"
                  "Available boilerplates are:")
            for key in boilerplates.keys():
                print(f"- {key}")
            quit()

    # setting new repo name
    repo_name = argv[1]

    # creating instance of github and of github user
    print("Connecting with Github.com")
    g = Github(token)
    user = g.get_user()

    # creating new repository
    print(f"Creating new repository: {repo_name}")
    repo = user.create_repo(repo_name)
    # checking for error (if repo name already exists for example)
    # TODO

    # create README
    readme = "# " + repo_name
    repo.create_file("README.md", "init commit", readme)

    # create all files depending on boilerplate
    if bool_boilerplate:
        print(f"Creating boilerplate: {boilerplate}")
        files = boilerplates[boilerplate]["Files"]
        [repo.create_file(file, "init commit", "") for file in files if files]

    # getting the new repo url
    repo_url = repo.git_url

    # cmd for cloning github repo
    cmd_clone = ["git", "clone", repo_url]
    # running the command
    subprocess.run(cmd_clone)

    # create empty folders locally, cannot have empty folders on github
    if bool_boilerplate:
        folders = boilerplates[boilerplate]["Empty_Folders"]
        [os.makedirs(repo_name + folder) for folder in folders if folders]

    print(f"Successfully created your new project {repo_name}")


def CRUD_boilerplates(name, boilerplates):
    print("# TODO: Create a CRUD function for boilerplates")


if __name__ == "__main__":
    main()
