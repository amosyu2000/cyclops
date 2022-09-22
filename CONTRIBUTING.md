# Contributing to Cyclops

| Table of Contents |
|---|
| [Setting up your Environment](#setting-up-your-environment) |
| [Creating an Issue](#creating-an-issue) |
| [Creating a New Branch](#creating-a-new-branch) |
| [Submitting a Pull Request](#submitting-a-pull-request) |
| [Reviewing a Pull Request](#reviewing-a-pull-request) |
| [Amending a Pull Request](#amending-a-pull-request) |

## Setting up your Environment

1. Set up Git on your computer.  
	- You can find a guide [here](https://docs.github.com/en/get-started/quickstart/set-up-git).
1. Clone the repository.  
	- Options for cloning can be found by clicking the __Code ▼__ button under the __Code__ tab of the GitHub repository.

_There are lots of IDEs available, but I recommend using Visual Studio Code because of its vast selection of plugins._

3. Download and install Visual Studio Code.  
1. Launch Visual Studio Code.  
1. Navigate to the Marketplace by clicking __Extensions__ on the left menu bar or typing __Ctrl+Shift+X__.  
1. Install GitLens from the Marketplace.  
1. Navigate to the Settings page by clicking __Manage → Settings__ on the left menu bar or typing __Ctrl+,__.  
1. Check the __Git: Allow Force Push__ checkbox.  
![image](https://user-images.githubusercontent.com/46848538/191061697-bde8ca67-25b4-4221-9dda-d51ea56cc1f4.png)

## Creating an Issue

_Issues are a way of reporting bugs/improvements and assigning the workload between all the members of the team. All work done by the team should have an associated issue._  

1. Navigate to the __Issues__ tab of the GitHub repository.  
1. Click __New Issue__.  
![image](https://user-images.githubusercontent.com/46848538/191032399-a52c5436-c84c-4a07-8919-abb0d314c93f.png)
1. Write a clear, concise title for the issue.  
1. Write any information relevant to the issue in the description, such as  
	- A more detailed description of the issue
	- Steps for reproducing (if it's a bug)
	- Error logs
	- Screenshots
	- Images
1. Add relevant labels to the issue. The most common labels are  
	- __bug__ - if something isn't working as intended
	- __enchancement__ - if a new feature is being implemented
	- __documentation__
1. Click __Submit New Issue__.  
![image](https://user-images.githubusercontent.com/46848538/191032810-3eca9f31-dcc8-402d-8805-4d3119c8cdb8.png)

## Creating a New Branch

_To begin working on an issue, the first step is creating a new branch to work on. If you intend to work on something that does not yet have an issue made for it, create a new issue first._  

1. Assign the issue to yourself.  
![image](https://user-images.githubusercontent.com/46848538/191033429-c63aefff-3282-410d-bacc-9d6a6b701803.png)
1. Navigate to the Source Control page by clicking __Source Control__ on the left menu bar or typing __Ctrl+Shift+G G__.  
1. Pull the __main__ branch to get the latest version.  
1. Create a new branch off of the __main__ branch.  
1. Name your new branch "`<macID>`/`<description>`".  
![image](https://user-images.githubusercontent.com/46848538/191035363-e939904e-9304-4822-bbfe-10755f32c051.png)
1. Switch to your new branch.  

## Submitting a Pull Request

_Once your code is ready to be merged, push it to remote repository and create a pull request._  

1. In Visual Studio Code, navigate to the Source Control page.  
1. Stage and commit your changes. Your commit message should include  
![image](https://user-images.githubusercontent.com/46848538/191038067-a3d7c7f3-2794-4ecb-8d33-0706f7c26a0b.png)
	- The issue number
	- A clear, concise title describing what was changed
	- If needed, a body explaining the changes in more detail
1. Publish your branch to the remote repository.  
![image](https://user-images.githubusercontent.com/46848538/191036680-aef8c46a-72bd-410c-89af-2790f8766205.png)
1. In GitHub, create a pull request for the branch.  
	- The title and description should auto-fill.
1. Add the __review__ label.  
![image](https://user-images.githubusercontent.com/46848538/191039209-01c9a947-56bf-4cf4-8850-821782f600d5.png)
1. Ask other contributors to review your pull request and approve it if looks good.  
1. Once your pull request gets approved and all review are resolved, merge the branch to main.  
	- Once your branch is merged, it is automatically deleted.
1. Once your pull request is merged, close the associated issue.  

## Reviewing a Pull Request

_Reviewing a pull request is the best way to double-check another person's work. Branches need a certain number of approvals on their pull request before they can be merged to main._  

1. In GitHub, familiarize yourself with the issue associated with the pull request.  
1. Look over the changes on the pull request.  
1. Optionally, checkout a branch in Visual Studio Code to poke around on it locally.  
![image](https://user-images.githubusercontent.com/46848538/191106450-7fcccf7a-ad07-41bc-9c94-9e662dcd38d7.png)
	- In Visual Studio Code, navigate to the Source Control page.
	- Click __… → Checkout to...__.
	- Select the desired branch.
1. In GitHub, create code reviews in the __Files changed__ tab of the pull request for any problems you see.  
![image](https://user-images.githubusercontent.com/46848538/191107966-70ef4b59-8c18-4a1b-9075-6894eef3ded1.png)
1. If everything looks good, approve the pull request.  
	- As a common courtesy, do not merge a pull request unless you are the author.

## Amending a Pull Request

_Sometimes you need to make additional changes after you've created a pull request._

1. In Visual Studio Code, navigate to the Source Control page.  
1. Stage your additional changes.  
1. Click __… → Commit → Commit Staged (Amend)__.  
![image](https://user-images.githubusercontent.com/46848538/191058215-ab62e0df-ad60-4c40-8fcc-90e9e1193184.png)
1. A tab named __COMMIT_EDITMSG__ will open. Here you can choose to also amend the commit message. Save and close this tab when you are done.  
![image](https://user-images.githubusercontent.com/46848538/191058700-7dbb6ace-8ce4-4294-ab61-0c2a64ae6a99.png)
1. Click __… → Pull, Push → Push (Force)__.  
![image](https://user-images.githubusercontent.com/46848538/191058844-b4d89fa7-fc05-4a31-a1a8-101dc4e7afd9.png)

_Your additional changes should now be reflected in your existing pull request under the same commit._  
