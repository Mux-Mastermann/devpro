# devpro

Create new projects on Github and clone it to your PC with just one line of code. Setup your new **dev**elopement **pro**jects in just a second.

## What's new?
- Added custom boilerplate creation ([Changelog](/CHANGELOG.md#110---2020-04-25))

## Features
- [x] Create repo on github and clone it to your local machine
- [x] Create a boilerplate of the needed file and folder structure
- [x] Make custom boilerplates for later use

## Prerequisites

To use this script `PyGitHub` needs to be installed on your system. If not already installed, you can install [PyGitHub](https://github.com/PyGithub/PyGithub) by typing the following in a terminal:
```
$ pip install PyGithub
```
You will also need a **Personal Access Token** from Github. A brief introduction on how to create a token can be found [Here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

After creating the token you should paste it inside the `credentials_template.py`:
```
token = "YOUR_PERSONAL_ACCESS_TOKEN"
```
Rename the file to `credentials.py`.

## Usage
This script will create a new Github Repository with the name you provide and will then clone it to your local machine, precisely inside the folder from which you run the command.

Usage:
```
$ devpro.py project_name
```
You can provide a second argument, which is called boilerplate. This will also create some standard files and folders for you depending on your project:
```
$ devpro.py project_name website
```
Devpro comes with two available boilerplates (**website** for static websites and **flask** for web applications), which are stored in a `boilerplates.json` file.

#### Custom boilerplates
As of **[v1.1](/CHANGELOG.md#110---2020-04-25)** you can create custom boilerplates. `$ cd` inside the folder, which contains your desired boilerplate files and folders. Then run the following command and make sure to replace `boilerplate_name` with the name you want to give to your custom boilerplate:
```
$ devpro.py boilerplate_name boilerplate
```
When you use the Keyword `boilerplate` as second command-line argument devpro will walk over all subfolders and files of your current working directory. The gathered structure will be stored as a new boilerplate in the boilerplates.json file. Hidden files, starting with a `.` will be ignored. A `.gitkeep` file will be added to all empty folders because you can't have empty folders on Github.


From now on you can use your newly created boilerplate just how in the example above:
```
$ devpro.py project_name boilerplate_name
```
You can open the `boilerplates.json` with any text editor to update or delete existing boilerplates.

Devpro boilerplates are for quickly creating the project structure not the content. Please be aware that any **files** created from a boilerplate **will be empty!**

---
**PLEASE NOTICE:**  
By default you can run python scripts **only from inside the folder where the script is located.**

Running python scripts from any directory on your machine highly depends on your operating system. I highly recommend to search google for something like:
> "running python scripts from anywhere under YOUR_OS"

The following instructions worked for me under Windows 10 and using customized [Hyper](https://hyper.is/) as command-line interface:
1. Add the path of the devpro directory to Windows "PATH" system variable:
   1. Open Explorer
   2. Right-click on "My Computer"
   3. Click "Properties"
   4. Click "Advanced system settings"
   5. Select tab "Advanced"
   6. Click "Environment Variables"
   7. Select "Path"
   8. Click "Edit"
   9. Click "New"
   10. Add path to the created directory, e.g "C:\Users\Your Name\devpro"
2. Mark the script as executable:
   1. `$ cd` inside the devpro folder.
   2. run `$ chmod +x devpro.py`.

## Credits
[@rpreissel](https://github.com/rpreissel) for knowing all the answers to my questions within a second and for leaving me a bit smarter than before after really every developer talk we have.

[@dmalan](https://github.com/dmalan) for taking me on an exciting ride through Computer Science and finally revealing that there is no magic happening under the hood. You are a great teacher!

[Corey Schafer](https://www.youtube.com/user/schafer5) for your great YouTube videos about Python.

---

This project (v1.0) was submitted as Final Project on the Harvard CS50x Introduction to Computer Science Course.
