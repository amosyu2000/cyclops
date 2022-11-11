<div align="center">

<a href="https://github.com/amosyu2000/cyclops">
	<img src="../../refs/header.svg" width="800" height="400" alt="Cyclops header">
</a>

# Development Plan <!-- omit in toc -->
Cyclops Ride Assist: Real-time bicycle crash detection and blindspot monitoring.<br/>  
__Team 9__  
Aaron Li (lia79)  
Amos Cheung (cheuny2)  
Amos Yu (yua25)  
Brian Le (leb7)  
Manny Lemos (lemosm1)  

</div>

<div style="page-break-after: always;"></div> <!-- Page Break -->

## Table of Contents <!-- omit in toc -->
- [1. Revision History](#1-revision-history)
- [2. Version Control](#2-version-control)
- [3. Roles and Responsibilities](#3-roles-and-responsibilities)
	- [3.1. Aaron Li](#31-aaron-li)
	- [3.2. Amos Cheung](#32-amos-cheung)
	- [3.3. Amos Yu](#33-amos-yu)
	- [3.4. Brian Le](#34-brian-le)
	- [3.5. Manny Lemos](#35-manny-lemos)
- [4. Team Communication Plan](#4-team-communication-plan)
- [5. Team Meeting Plan](#5-team-meeting-plan)
- [6. Git Workflow Plan](#6-git-workflow-plan)
- [7. Overall System Workflow Plan](#7-overall-system-workflow-plan)
- [8. Proof of Concept Demonstration Plan](#8-proof-of-concept-demonstration-plan)
- [9. Software Development and Engineering Tools and Technology](#9-software-development-and-engineering-tools-and-technology)
- [10. Handling Changes](#10-handling-changes)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)

## List of Figures <!-- omit in toc -->

## 1. Revision History
<div align="center">

<p id="rh">Table 1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2022-09-22 | Brian Le | Document created |
| 2022-09-23 | Brian Le | Detailed steps and tools |
| 2022-10-20 | Amos Yu | Improved formatting |
| 2022-11-09 | Aaron Li | Updated content |
</div>

## 2. Version Control

Team members are expected to use the private Github repository. Team members will also be expected to maintain repos containing clean and accurate code. Members are required to create new branches when developing different aspects of software before merging into the main branch once functionality has been verified and is stable. Changes are highly encouraged to be made through multiple commits with a new commit made for per module or per 50 lines of code. Pull Requests are to be processed with the validation of at least two other members within the team with discussions encouraged to be held within their respective topics.

## 3. Roles and Responsibilities

### 3.1. Aaron Li

- Responsible for the design of mounting and the physical components of Cyclops
- Ensuring the seamless integration of electrical and mechanical components

### 3.2. Amos Cheung

- Responsible for the design of the electrical components of Cyclops
- Ensure accurate reading of accelerometer and/or gyroscope 

### 3.3. Amos Yu

- Responsible for crash detection module for Cyclops
- Ensuring that proper logging system is in place

### 3.4. Brian Le

- Responsible for blindspot detection module for Cyclops
- Ensuring proper vehicle and cyclist detection

### 3.5. Manny Lemos

- Responsible for sensor and camera module of Cyclops
- Ensuring proper communication between the crash detection and blindspot detection module for Cyclops


## 4. Team Communication Plan
The team will be communicating primarily using Facebook Messenger. This application allows the team to instantly send messages to one another. Furthermore, notifications have been enabled to ensure that each team member receives an alert. In person meetings will be held as well as a way to discuss progress and issues as the development of the project continues. This will be further discussed in Section 5 - Team Meeting Plan. Team member will be expected to communicate frequently and as timely as possible with one another. In the case of an emergency, personal contact information has been distributed between the team members. In the case of conflicts, the team will discuss privately as one to determine the course of action. 

## 5. Team Meeting Plan
The team will be meeting once a week officially every Tuesday from 2:30 - 3:30pm at a McMaster location or house. During these meetings, there will be a time to present the progress that has been done on the previous meeting's agenda and checklist. Furthermore, next steps for the development will be discussed and addressed with each member receiving an equal amount of work for the week. All members are expected to be done their part by the next meeting. All members are expected to be timely for each meeting. In the case that a member cannot make a meeting, they must use the official team communication application, Facebook Messenger, to alert the team of their absence. They will still be expected to complete their portion of work for the week. At the team meeting, each member will have an opportunity to ask questions to one another in order to further the understanding of the overall project. One of the team members will be responsible for taking notes using the formatting outlined in the Github Wiki. These notes will be made available in the Github Discussions tab.  


## 6. Git Workflow Plan

Team members of Cyclops are expected to follow this general outline as a workflow:

 1. Before beginning work on a new module, pull any new changes from the master branch.
 2. Create a new branch to develop on if a branch doesn't already exist for this module.
 3. Create a detailed plan of the structure of the module. 
 4. Implement the modules/functions.
 5. Perform unit testing on the modules and its functions.
 6. Push any changes to the current working branch.
 7. Repeats steps 4 through 6 towards the completion of the module.
 8. Merge new functionality to the Master branch after code review from 2 other team members.

This workflow will be manual. 

## 7. Overall System Workflow Plan

The following are steps that the Cyclops team aim to complete:

 1. Create CAD designs, using AutoCAD Inventor.
 2. Build base of Cyclops mount to support electrical and mechanical components.
 3. Build gyroscopic system with relevant electrical components and Raspberry Pi environment for the crash detection system.
 4. Gather feature set of vehicles to train models on vehicle recognition within the blindspot detection system. 
 5. Build blindspot detection system with relevant sensor and computer vision components with Python IDE.
 6. Implement crash logging system for Cyclops.
 7. Implement communication between the crash detection system, blindspot detection system and the crash logging system.
 8. Assemble closed physical system.


## 8. Proof of Concept Demonstration Plan
Cyclops Ride Assist is a complex electromechanical system with software and hardware interfacing. There are many risks that will need to be addressed before the Proof of Concept Demonstration. Some of these risks include learning Python and the Raspberry Pi IDE and using the OpenCV library, creating datasets and training machine learning models to accurately detect vehicles, and merging mechanical and electrical components to create one unified design and product. 
The Proof of Concept demonstration will consist of the following main components:
1. Breadboard Prototype: The breadboard will be shown with the existing wires and connections to the Raspberry Pi. The breadboard will be neat and exhibit a high level of understanding of electrical concepts. 
2. Accelerometer: The accelerometer will be wired correctly to the Rasperrry Pi and will be able to output data into a Python graph using numpy. 
3. Car Recognition: The system will be able to detect cars. There will be footage of the prototype working with a real-size car as well as a demonstration of an audiovisual cue on the breadboard when a model car is shown in person. 
4. 3D Modelling: The first iteration of the design will be shown to house the Raspberry Pi safely. The housing and the files will be presented. 
5. Front-facing Camera: There will be a demonstratino of the front camera saving a certain amount of footage. 
6. Battery Power: The Raspberry Pi being powered by battery will be shown. 
7. Any additional development tools will be discussed. 

## 9. Software Development and Engineering Tools and Technology

The following are environments, tools, and technologies that team members will be using for the creation, development, and debugging of the system:

Software:
 - Python: Python will be the main programming language used. 
 - OpenCV: OpenCV will be the primary machine learning library used to help test vehicle detection.   
 - NumPy: NumPy will be a Python library used to develop the graphs of the accelerometer data. 
 - PyTest: PyTest will be used as the main testing tool for the software components. 
 - Visual Studio Code (VSCode): VSCode will be the preferred Python and Github IDE and will be utilized for computer vision, video log development.
 - Raspberry Pi IDE: Will be used for the development of the crash detection system.
 - MobaXTerm: MobaXTerm will be used for SSH purposes for remote connections between computers and the Raspberry Pi. 
 - Github: Github will be the version control and issue tracking platform utilized. 
 - Markdown: Markdown will be the primary text-based language used to create documentation. 

Hardware:
 - Prusa MK3: Will be used to create the 3D models for testing and final product. 
 - Autodesk Inventor: Inventor will be utilized for creating 3D models for the physical aspects of Cyclops including the mount and housing. 
 - Autodesk EAGLE: EAGLE will be used to design the PCB electrical schematic. 
 - Printed Circuit Board (PCB): A PCB will be used for all electrical components and will contain soldered parts. Cables and resistors will be provided by the team. 
 - Bike: Tester bike will be used to simulate and test the functionalities of Cyclops in a real time environment.
 - Webcam: A webcam will be used as a camera for both front and back-facing camera. 
 - Machining Tools: A variety of machining tools will be used in order to create the electro-mechanical system. For example, power drills, screwdrivers, soldering irons, etc. 

## 10. Handling Changes

Team members will also be encouraged to follow the format within **CONTRIBUTING.md**:

 1. Create an issue in the Github page.
 2. Create a new branch if necessary with the name of the change. 
 3. Perform unit testings to verify that the issue is still prevalent.
 4. Perform regression testing to ensure that there are no further issues appearing.
 5. Merge to the Master branch.
 6. Close the issue.


