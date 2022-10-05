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
    - [3.2.1 Naming Conventions](#321-naming-conventions)
    - [3.2.2 Constants](#322-constants)
    - [3.2.3 Monitored Variables](#323-monitored-variables)
    - [3.2.4 Controlled Variables](#324-controlled-variables)
  - [3.3 Relevant Facts and Assumptions](#33-relevant-facts-and-assumptions)
    - [3.3.1 Relevant Facts](#331-relevant-facts)
    - [3.3.2 Assumptions](#332-assumptions)
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
add content
### 2.2 Project Scope
add content
### 2.3 Behaviour Overview
add content
### 2.4 Project Stakeholders
add content
### 2.5 Product Users
add content

## 3 Project Constraints
add content
### 3.1 Mandated Constraints
A list of constraints which will adhered to during the design and development of this system.

**Mandated Constraint 1:**  
This capstone project must be completed prior to the final demonstration.  
**Rationale 1:**  
Project deadlines provided in the course outline dictate project milestone which must be met. One such milestone is the final demonstration which occurs between March 20-31 2023.  

**Mandated Constraint 2:**  
The total cost of the components used in this design must not exceed $750.  
**Rationale 2:**  
The final deliverable must be a competitor in the open market. Further, using funds to purchase an off-the-shelf product is not allowed.  

**Mandated Constraint 3:**  
The system must be able to analyze inputs to produce desired results in real time.  
**Rationale 3:**  
Real time analysis and response is an integral component of the cyclops ride assist system. More precisely, desired results are only of value if they can be delivered on time every time.  

### 3.2 Naming Conventions and Definitions
#### 3.2.1 Naming Conventions
#### 3.2.2 Constants
- Gravity = 9.81 m/s<sup>2</sup>
#### 3.2.3 Monitored Variables
| Monitor Name | Monitor Description                                                                            | Monitor Type | Units  |
|--------------|------------------------------------------------------------------------------------------------|--------------|--------|
| αx           | Measures acceleration parallel to the path of  the bicycle.                                    | acceleration | m/s2   |
| αy           | Measures acceleration perpendicular to the path of  the bicycle along the plane of the ground. | acceleration | m/s2   |
| αz           | Measures acceleration in the vertical direction.                                               | acceleration | m/s2   |
| tilt         | Measures the vertical tilt of the system relative to a calibrated absolute level.              | rotation     | rad    |
| vfront       | Video feed from the front facing camera.                                                       | Video        | N/A    |
| vrear        | Video feed from the rear facing camera.                                                        | Video        | N/A    |
#### 3.2.4 Controlled Variables
| Controlled Name | Controlled Description                             | Controlled Type | Units  |
|-----------------|----------------------------------------------------|-----------------|--------|
| led_blind_spot  | Indicates a vehicle is in the bicycles blind spot. | Boolean        | N/A    |
### 3.3 Relevant Facts and Assumptions  
#### 3.3.1 Relevant Facts  
- example fact 1
#### 3.3.2 Assumptions  
Assumptions will enable developers to cull the scope of the problem(s) being undertaken. As such, assumptions will detail limitations of the system.  
**Assumption 1:**  
Cyclists will mount and dismount their bikes with care.  
**Rationale 1:**  
Violent mounting and dismounting of one's bicycle may result in unintended triggering of crash detection and subsequent video logging. The system will not be able to distinguish between violent (dis)mounting and true crashes.  

**Assumption 2:**  
While on the road, cyclists will abide by traffic laws. This means travelling in marked bike lanes where available.  
**Rationale 2:**  
The system will not be able to distinguish between parked vehicles, which may appear momentarily in a cyclists blind-spot, and moving vehicles. As a result, if a cyclist is not travelling in designated bike lanes they may be subject to increased instances of false blind-spot detection triggers.  

## 4 Context Diagrams  
![System Context Diagram](https://user-images.githubusercontent.com/68861121/193955661-d965823f-079b-444f-9cb3-cf34a120ac87.png)  
## 5 Functional Decomposition Diagrams
![User Diagram](https://user-images.githubusercontent.com/46848538/194148017-fdbf2709-8ab7-48b0-b066-e4e0d635e83c.png)  
![Data Flow Diagram](https://user-images.githubusercontent.com/46848538/194148013-97d6cb1a-f581-4c00-907a-5f27c3ee9485.png)  
![Legend](https://user-images.githubusercontent.com/46848538/194148016-d0cf9829-a4b2-468f-9141-8821ec97a692.png)  
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
**INNOVV ThirdEYE**  
INNOVV ThirdEYE is a blindspot detection system for motorcycles that uses sensors to determine if there are any objects close to the user. It can be either used through a mirror lens or a watch.   
https://www.innovv.com/innovv-thirdeye  
**Senzar Motorcycle Sensor**  
The Senzar Motorcycle Sensor is another system that uses LEDs, vibration, and radar sensors.  
https://meetsenzar.com/pages/senzar-m1-motorcycle-bsm

### 8.3 Risks
1. Components (sensor, camera) will deteriorate over time, leading to inaccuracies.
2. Components can be damaged in case of a cycle crash.
3. Incorrect image (car vs a tree) is read through Computer Vision, leading to inaccuracies.
4. Storage space is exceeded or becomes corrupted.
### 8.4 Costs
1. Raspberry PI Robot
2. Sensors
3. Cameras
4. 3D Printed Mount and Storage System
5. Cables/Wires
6. Bicycle
## 9 Changes
### 9.1 Likely Changes
### 9.2 Unlikely Changes

