# Development Plan
Group 9
 - Aaron Li - lia79
 - Amos Cheung - cheuny2
 - Amos Yu - yua25
 - Brian Le - leb7
 - Manny Lemos - lemosm1

# 1 Revisions

<div style="text-align: center;"> 
    <p id="Revision_History">
        Table 1: Revision History
        <table style="width: 100%; text-align: left;">
            <tr>
                <th>Date</th>
                <th>Developer(s)</th>
                <th>Change</th>
            </tr>
            <tr>
                <td>2022-09-22</th>
                <td>Brian Le</th>
                <td>Document Created</th>
            </tr>
            <tr>
                <td>2022-09-23</th>
                <td>Brian Le</th>
                <td>Detailed steps and tools</th>
            </tr>
        </table>
    </p>
</div>

# 2 Version Control

Team members are expected to use the private Github repository. Team members will also be expected to maintain repos containing clean and accurate code. Members are required to create new branches when developing different aspects of software before merging into the main branch once functionality has been verified and is stable. Changes are highly encouraged to be made through multiple commits with a new commit made for per module or per 50 lines of code. Pull Requests are to be processed with the validation of at least two other members within the team with discussions encouraged to be held within their respective topics.

# Roles and Responsibilities

## Aaron Li

- Responsible for the design of mounting and the physical components of Cyclops
- Ensuring the seamless integration of electrical and mechanical components

## Amos Cheung

- Responsible for the design of the electrical components of Cyclops
- Ensure accurate reading of accelerometer and/or gyroscope 

## Amos Yu

- Responsible for crash detection module for Cyclops
- Ensuring that proper logging system is in place

## Brian Le

- Responsible for blindspot detection module for Cyclops
- Ensuring proper vehicle and cyclist detection

## Manny Lemos

- Responsible for sensor and camera module of Cyclops
- Ensuring proper communication between the crash detection and blindspot detection module for Cyclops


# Process Workflow

Team members of Cyclops are expected to follow this general outline as a workflow:

 1. Before beginning work on a new module, pull any new changes from the master branch.
 2. Create a new branch to develop on if a branch doesn't already exist for this module.
 3. Create a detailed plan of the structure of the module. 
 4. Implement the modules/functions.
 5. Perform unit testing on the modules and its functions.
 6. Push any changes to the current working branch.
 7. Repeats steps 4 through 6 towards the completion of the module.
 8. Merge new functionality to the Master branch after code review from 2 other team members.

# Details on Steps to be Taken

The following are steps that the Cyclops team aim to complete:

 1. Create CAD designs, using Inventor or SolidWorks.
 2. Build base of Cyclops mount to support electrical and mechanical components.
 3. Build gyroscopic system with relevant electrical components and Arduino environment for the crash detection system.
 4. Gather feature set of vehicles to train models on vehicle recognition within the blindspot detection system. 
 5. Build blindspot detection system with relevant sensor and computer vision components with Python IDE.
 6. Implement crash logging system for Cyclops.
 7. Implement communication between the crash detection system, blindspot detection system and the crash logging system.
 8. Assemble closed physical system.

# Development Tools

The following are environments that team members will be using for the development and debugging of the system:

 - Visual Studio Code: Utilized for computer vision and video log development.
 - Arduino IDE: Will be used for the development of the crash detection system.
 - Autodesk Inventor: Utilized for creating 3D models for the physical aspects of Cyclops including the mount and chassis. 
 - Github: The version control and issue tracking platform utilized. 
 - Bike: Tester bike will be used to simulate and test the functionalities of Cyclops in a real time environment.

# Handling Changes

Team members will also be encouraged to follow the format within **CONTRIBUTING.md**:

 1. Create an issue in the Github page.
 2. Create a new branch if necessary with the name of the change. 
 3. Perform unit testings to verify that the issue is still prevalent.
 4. Perform regression testing to ensure that there are no further issues appearing.
 5. Merge to the Master branch.
 6. Close the issue

