<!--Title Page-->
<div style="text-align: center;"> 
    <h1 id="Document_Title">Software Requirements Specification for Cyclops:</h1>
    <h2 id="Document Description">Real-time bicycle crash detection and blindspot monitoring</h2>
    <h4 id="Group_Info">Group 9</h4>
    <h4 id="Author_Info">
        Aaron Li    - lia79     <br>
        Amos Cheung - cheuny2   <br>
        Amos Yu     - yua25     <br>
        Brian Le    - leb7      <br>
        Manny Lemos - lemosm1   <br>
    </h4>
</div>

<!--Page Break-->
<div style="page-break-after: always;"></div>

<!-- Table of Contents-->
# Table of Contents <!-- omit in toc -->
- [1 Revisions](#1-revisions)
- [2 Project Drivers](#2-project-drivers)
  - [2.1 Project Purpose](#21-project-purpose)
  - [2.2 Project Scope](#22-project-scope)
  - [2.3 Behaviour Overview](#23-behaviour-overview)
  - [2.4 Project Stakeholders](#24-project-stakeholders)
  - [2.5 Product Users](#25-product-users)
- [3 Project Constraints](#3-project-constraints)
  - [3.1 Mandated Constraints](#31-mandated-constraints)
  - [3.2 Naming Conventions and Definitions](#32-naming-conventions-and-definitions)
  - [3.3 Relevant Facts and Assumptions](#33-relevant-facts-and-assumptions)
- [4 Context Diagrams](#4-context-diagrams)
- [5 Functional Decomposition Diagrams](#5-functional-decomposition-diagrams)
- [6 Functional Requirements](#6-functional-requirements)
  - [6.1 Scope of Work](#61-scope-of-work)
  - [6.2 Business Data Model and Data Dictionary](#62-business-data-model-and-data-dictionary)
  - [6.3 Scope of the Product](#63-scope-of-the-product)
  - [6.4 Functional Requirements](#64-functional-requirements)
- [7 Non-Functional Requirements](#7-non-functional-requirements)
  - [7.1 Look and Feel Requirements](#71-look-and-feel-requirements)
    - [7.1.1 Appearance Requirements](#711-appearance-requirements)
    - [7.1.2 Style Requirements](#712-style-requirements)
  - [7.2 Usability and Humanity Requirements](#72-usability-and-humanity-requirements)
    - [7.2.1 Ease of Use Requirements](#721-ease-of-use-requirements)
    - [7.2.2 Personalization and Internationalization Requirements](#722-personalization-and-internationalization-requirements)
    - [7.2.3 Learning Requirements](#723-learning-requirements)
    - [7.2.4 Understandability and Politeness Requirements](#724-understandability-and-politeness-requirements)
    - [7.2.5 Accessibility Requirements](#725-accessibility-requirements)
  - [7.3 Performance Requirements](#73-performance-requirements)
    - [7.3.1 Speed and Latency Requirements](#731-speed-and-latency-requirements)
    - [7.3.2 Safety-Critical Requirements](#732-safety-critical-requirements)
    - [7.3.3 Precision and Accuracy Requirements](#733-precision-and-accuracy-requirements)
    - [7.3.4 Reliability and Availability Requirements](#734-reliability-and-availability-requirements)
    - [7.3.5 Robustness or Fault-Tolerance Requirements](#735-robustness-or-fault-tolerance-requirements)
    - [7.3.6 Capacity Requirements](#736-capacity-requirements)
    - [7.3.7 Scalability and Extensibility Requirements](#737-scalability-and-extensibility-requirements)
    - [7.3.8 Longevity Requirements](#738-longevity-requirements)
  - [7.4 Optional and Environmental Requirements](#74-optional-and-environmental-requirements)
    - [7.4.1 Expected Physical Environemnt](#741-expected-physical-environemnt)
    - [7.4.2 Environmental Impact Requirements](#742-environmental-impact-requirements)
  - [7.5 Maintainability and Support Requirements](#75-maintainability-and-support-requirements)
    - [7.5.1 Change Requirements](#751-change-requirements)
    - [7.5.2 Requirements for Interfacing with Adjacent Systems](#752-requirements-for-interfacing-with-adjacent-systems)
    - [7.5.3 Productization Requirements](#753-productization-requirements)
    - [7.5.4 Release Requirements](#754-release-requirements)
    - [7.5.5 Longevity Requirements](#755-longevity-requirements)
  - [7.6 Security Requirements](#76-security-requirements)
    - [7.6.1 Privacy Requirements](#761-privacy-requirements)
    - [7.6.1 Privacy Requirements](#761-privacy-requirements-1)
  - [7.7 Cultural and Political Requirements](#77-cultural-and-political-requirements)
    - [7.7.1  Requirements](#771--requirements)
  - [7.8 Legal Requirements](#78-legal-requirements)
  - [7.8.1 Legal Release Requirements](#781-legal-release-requirements)
- [8 Project Issues](#8-project-issues)
  - [8.1 Open Issues](#81-open-issues)
  - [8.2 Off-the-Shelf Solutions](#82-off-the-shelf-solutions)
    - [INNOVV ThirdEYE](#innovv-thirdeye)
    - [Senzar Motorcycle Sensor](#senzar-motorcycle-sensor)
  - [8.3 Risks](#83-risks)
  - [8.4 Costs](#84-costs)
- [9 Changes](#9-changes)
  - [9.1 Likely Changes](#91-likely-changes)
  - [9.2 Unlikely Changes](#92-unlikely-changes)

<!--Page Break-->
<div style="page-break-after: always;"></div>

<!--Revision History-->
## 1 Revisions
<table style="width: 100%; text-align: left;">
    <tr>
        <th>Date</th>
        <th>Developer(s)</th>
        <th>Change</th>
    </tr>
    <tr>
        <td>2022-10-03</th>
        <td>Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos</th>
        <td>Document Created</th>
    </tr>
</table>

<!--Page Break-->
<div style="page-break-after: always;"></div>

## 2 Project Drivers
### 2.1 Project Purpose
The purpose of this project is to create a system that helps cyclists to have a more secured experience especially on roads without bike lanes.

Cyclops Ride Assist (CRA) is going to be an all-in-one, easily mountable, and quick to setup system that adds modern car safety features onto a bike, such as blind spot detection and crash detection. The system will also have a built in headlamp that will illuminate during night time, not just for the cyclist to see but also for cars around to realize the bike. 
### 2.2 Project Scope
CRA is going to be a bike assist system with convenient mounting, accurate crash detection, video buffering and saving, reliable blindspot monitoring and a user controlled headlamp that helps cyclist to have a peace of mind while riding on the road. Although CRA is primarily targeted towards road cyclists, it will able be useful for cyclists who ride on mountains or trails.
### 2.3 Behaviour Overview
The user can press the power button to turn on the CRA. Once it turns on, it will start to record the forward point of view of the bike. If a bike crash is detected, the system will store the past five minutes of footage so the user can look back at the events leading up to the crash. Also on the back side of the system, CRA will watch out for cars approaching the bike at blind spots and alert the cyclist with an indicator. The system also has a headlamp that is easily switched on and off for dark environment.
### 2.4 Project Stakeholders
The project stakeholders are as follows:  
- The project proposers (Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos)
- The project supervisor (Dr Spencer Smith)
- The teaching assistants (Nicholas Annable)
- The user (cyclist)
### 2.5 Product Users
The user will be all cyclists.
## 3 Project Constraints
add content
### 3.1 Mandated Constraints
add content
### 3.2 Naming Conventions and Definitions
add content
### 3.3 Relevant Facts and Assumptions
add content
## 4 Context Diagrams
## 5 Functional Decomposition Diagrams
## 6 Functional Requirements
### 6.1 Scope of Work
### 6.2 Business Data Model and Data Dictionary
### 6.3 Scope of the Product
### 6.4 Functional Requirements
## 7 Non-Functional Requirements
### 7.1 Look and Feel Requirements
#### 7.1.1 Appearance Requirements 
#### 7.1.2 Style Requirements 
### 7.2 Usability and Humanity Requirements
#### 7.2.1 Ease of Use Requirements 
#### 7.2.2 Personalization and Internationalization Requirements
#### 7.2.3 Learning Requirements 
#### 7.2.4 Understandability and Politeness Requirements 
#### 7.2.5 Accessibility Requirements 
### 7.3 Performance Requirements
#### 7.3.1 Speed and Latency Requirements 
#### 7.3.2 Safety-Critical Requirements 
#### 7.3.3 Precision and Accuracy Requirements 
#### 7.3.4 Reliability and Availability Requirements 
#### 7.3.5 Robustness or Fault-Tolerance Requirements 
#### 7.3.6 Capacity Requirements 
#### 7.3.7 Scalability and Extensibility Requirements 
#### 7.3.8 Longevity Requirements 
### 7.4 Optional and Environmental Requirements
#### 7.4.1 Expected Physical Environemnt 
#### 7.4.2 Environmental Impact Requirements
### 7.5 Maintainability and Support Requirements
#### 7.5.1 Change Requirements
#### 7.5.2 Requirements for Interfacing with Adjacent Systems
#### 7.5.3 Productization Requirements 
#### 7.5.4 Release Requirements 
#### 7.5.5 Longevity Requirements 
### 7.6 Security Requirements
#### 7.6.1 Privacy Requirements
#### 7.6.1 Privacy Requirements

### 7.7 Cultural and Political Requirements
#### 7.7.1  Requirements

### 7.8 Legal Requirements
### 7.8.1 Legal Release Requirements
## 8 Project Issues
### 8.1 Open Issues
1.) Creating accurate documentation for the system specifications.
2.) Starting to develop the software, purchasing some hardware to begin system creation.
### 8.2 Off-the-Shelf Solutions
#### INNOVV ThirdEYE
INNOVV ThirdEYE is a blindspot detection system for motorcycles that uses sensors to determine if there are any objects close to the user. It can be either used through a mirror lens or a watch. 
https://www.innovv.com/innovv-thirdeye
#### Senzar Motorcycle Sensor
The Senzar Motorcycle Sensor is another system that uses LEDs, vibration, and radar sensors. 
https://meetsenzar.com/pages/senzar-m1-motorcycle-bsm

### 8.3 Risks
1.) Components (sensor, camera) will deteriorate over time, leading to inaccuracies.
2.) Components can be damaged in case of a cycle crash.
3.) Incorrect image (car vs a tree) is read through Computer Vision, leading to inaccuracies.
4.) Storage space is exceeded or becomes corrupted.
### 8.4 Costs
1.) Raspberry PI Robot
2.) Sensors
3.) Cameras
4.) 3D Printed Mount and Storage System
5.) Cables/Wires
6.) Bicycle
## 9 Changes
### 9.1 Likely Changes
### 9.2 Unlikely Changes

