#! python

import subprocess
import json
import os

from github import Github
from credentials import token
from sys import argv


# getting the location of the devpro script
script_dir = os.path.dirname(__file__)


def main():
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
            # Run create function for the boilerplate
            create_boilerplates(argv[1], boilerplates)
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
        files = boilerplates[boilerplate]["Empty_Folders"]
        [repo.create_file(file, "init commit", "") for file in files if files]

    # getting the new repo url
    repo_url = repo.git_url

    # cmd for cloning github repo
    cmd_clone = ["git", "clone", repo_url]
    # running the command
    subprocess.run(cmd_clone)
    # Printing Success-Message
    print(f"Successfully created your new project {repo_name}")


def create_boilerplates(name, boilerplates):
    # check if boilerplate already exists
    if name in boilerplates.keys():
        print(f"Boilerplate '{name}' already exists.")
        print("Do you want to open the boilerplate.json to edit or delete?")
        answer = input()
        if answer.lower() in ["yes", "y"]:
            # Open boilerplates.json
            os.system(f"notepad {script_dir}/boilerplates.json")
        quit()

    # create new boilerplate:
    add_files = []
    add_folders = []
    # get index of the root directory
    slicer = len(os.getcwd()) + 1
    # walk trough all directories in current working directory
    for path, dirs, files in os.walk(os.getcwd(), topdown=True):
        # removing hidden folders (starting with ".")
        dirs[:] = [d for d in dirs if not d.startswith(".")]
        # replacing backslash with slash
        path = path.replace("\\", "/")

        # check if files in dir
        if files:
            # check if not the root path
            if not path[slicer:]:
                # add all files from this directory to append list
                add_files.extend(files)
            else:
                # add path to the file, then add it to append list
                add_files.extend([path[slicer:] + "/" + file
                                  for file in files])
            # go to next dir
            continue
        elif not dirs:
            # if empty folder add '.gitkeep' file. Github cant store empty dirs
            add_folders.append(path[slicer:] + "/.gitkeep")
    # add files and folders to a new key in boilerplates dict
    boilerplates.update({name: {"Files": add_files,
                                "Empty_Folders": add_folders}})
    # serialize boilerplates dict back to boilerplates.json
    with open(script_dir + "/boilerplates.json", "w") as write_file:
        json.dump(boilerplates, write_file, indent=4)
    print(f"Boilerplate '{name}' successfully created!")


if __name__ == "__main__":
    main()
