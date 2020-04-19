# devpro

Create new projects on Github and clone it to your PC with just one line of code. Setup your new **dev**elopement **pro**jects in just a second.

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
$ devpro.py My_New_Project
```
By default you can run this script **only from inside the folder where the script is located.**

---
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

## Features
- [x] creating project folder and empty README on github and cloning it to your local machine
- [ ] included second command-line argument for project related folder and file creation (e.g. automatic creation of standard files and folders for a static website)
  - [ ] Static website
  - [ ] Flask web application

## Credits
@rpreissel for knowing all the answers to my questions within a second and for leaving me a bit smarter than before after really every developer talk we have.

[Corey Schafer](https://www.youtube.com/user/schafer5) for your great YouTube videos about Python.
 
