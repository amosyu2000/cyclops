<!--Title Page-->
<div style="text-align: center;"> 
    <h1 id="Document_Title">Software Requirements Specification for Cyclops Ride Assist</h1>
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
## Table of Contents <!-- omit in toc -->
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
  - [7.4 Operational and Environmental Requirements](#74-operational-and-environmental-requirements)
    - [7.4.1 Expected Physical Environment](#741-expected-physical-environment)
    - [7.4.2 Requirements for Interfacing with Adjacent Systems](#742-requirements-for-interfacing-with-adjacent-systems)
    - [7.4.3 Productization Requirements](#743-productization-requirements)
    - [7.4.4 Release Requirements](#744-release-requirements)
  - [7.5 Maintainability and Support Requirements](#75-maintainability-and-support-requirements)
    - [7.5.1 Maintenance Requirements](#751-maintenance-requirements)
    - [7.5.2 Supportability Requirements](#752-supportability-requirements)
    - [7.5.3 Adaptability Requirements](#753-adaptability-requirements)
  - [7.6 Security Requirements](#76-security-requirements)
    - [7.6.1 Access Requirements](#761-access-requirements)
    - [7.6.2 Integrity Requirements](#762-integrity-requirements)
    - [7.6.3 Privacy Requirements](#763-privacy-requirements)
    - [7.6.4 Audit Requirements](#764-audit-requirements)
    - [7.6.1 Immunity Requirements](#761-immunity-requirements)
  - [7.7 Cultural and Political Requirements](#77-cultural-and-political-requirements)
    - [7.7.1 Cultural Requirements](#771-cultural-requirements)
  - [7.8 Legal Requirements](#78-legal-requirements)
    - [7.8.1 Compliance Requirements](#781-compliance-requirements)
    - [7.8.2 Standards Requirements](#782-standards-requirements)
- [8 Project Issues](#8-project-issues)
  - [8.1 Open Issues](#81-open-issues)
  - [8.2 Off-the-Shelf Solutions](#82-off-the-shelf-solutions)
  - [8.3 Risks](#83-risks)
  - [8.4 Costs](#84-costs)
- [9 Changes](#9-changes)
  - [9.1 Likely Changes](#91-likely-changes)
  - [9.2 Unlikely Changes](#92-unlikely-changes)

## List of Tables <!-- omit in toc -->

## List of Figures <!-- omit in toc -->
- [Figure 4.1: CRA System Context Diagram](https://user-images.githubusercontent.com/68861121/193955661-d965823f-079b-444f-9cb3-cf34a120ac87.png)  
- [Figure 5.1: CRA Functional Decomposition Diagram](https://user-images.githubusercontent.com/46848538/194148017-fdbf2709-8ab7-48b0-b066-e4e0d635e83c.png)  
- [Figure 5.2: CRA Data Flow Diagram](https://user-images.githubusercontent.com/46848538/194148013-97d6cb1a-f581-4c00-907a-5f27c3ee9485.png)  
- [Figure 5.3: Legend for the CRA Data Flow Diagram](https://user-images.githubusercontent.com/46848538/194148016-d0cf9829-a4b2-468f-9141-8821ec97a692.png)  

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
Client: see User.  
CRA: abbreviation for Cyclops Ride Assist.  
Cyclist: a person who operates a bicycle as a means of transportation.  
User: a person who will operate the final product. See Cyclist.  

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
![image](https://user-images.githubusercontent.com/68861121/193955661-d965823f-079b-444f-9cb3-cf34a120ac87.png)  
Figure 4.1: CRA System Context Diagram
## 5 Functional Decomposition Diagrams
![image](https://user-images.githubusercontent.com/46848538/194148017-fdbf2709-8ab7-48b0-b066-e4e0d635e83c.png)  
Figure 5.1: CRA Functional Decomposition Diagram  
![image](https://user-images.githubusercontent.com/46848538/194148013-97d6cb1a-f581-4c00-907a-5f27c3ee9485.png)  
Figure 5.2: CRA Data Flow Diagram  
![image](https://user-images.githubusercontent.com/46848538/194148016-d0cf9829-a4b2-468f-9141-8821ec97a692.png)  
Figure 5.3: Legend for the CRA Data Flow Diagram  
## 6 Functional Requirements
### 6.1 Scope of Work
### 6.2 Business Data Model and Data Dictionary
### 6.3 Scope of the Product
### 6.4 Functional Requirements
## 7 Non-Functional Requirements
### 7.1 Look and Feel Requirements
#### 7.1.1 Appearance Requirements 
NFR1   
- The appearance of Cyclops Ride Assist will be white. This is to act as a safety mechanism to allow the bicycle/motorbike to be more visible at night.
NFR2   
- Cyclops Ride Assist will be contained in a mechanically created system mounted on the bicycle. This is to ensure that the the components will not interfere with the system or with the physical bicycle itself.
NFR3  
- There will be no offensive painting or colours on Cyclops Ride Assist. This is to ensure that no one is offended by the design style.   
#### 7.1.2 Style Requirements 
NFR4  
- Cyclops Ride Assist will be non-bulky and constructed in a minimalist way. This is to ensure that the system does not become distracting for the users or others on the road.
### 7.2 Usability and Humanity Requirements
#### 7.2.1 Ease of Use Requirements 
NFR5  
- Cyclops Ride Assist can be easily attached to the bicycle with minimal effort. This is to ensure that the user will want to and find it easy to use the product. 
NFR6  
- The software application of Cyclops Ride Assist will allow for a minimal amount of clicks or touches. This will allow users to easily access the files and videos they require.
NFR7  
- Cyclops Ride Assist will be designed in a way that can be easily understood and used by teenagers and adults for their own bicycles. This is to ensure that the system can be understood easily by different age groups. 
NFR8  
- Cyclops Ride Assist will be able to be used by people with minimal education or training. This is to ensure that the system can be understood easily by different educational groups. 
#### 7.2.2 Personalization and Internationalization Requirements
NFR9  
- Users will be able to make small modifications to Cyclops Ride Assist. This is needed so that users can make adjustments to allow the system to better fit their own personal bicycle.
#### 7.2.3 Learning Requirements 
NFR10  
- Cyclops Ride Assist shall be easy for anyone to learn within a short time. This is so that anyone can use the system easily.
NFR11  
- Cyclops Ride Assist will be able to be created by an engineer with one week of training. This is so that any engineer can upgrade or perform maintenance on the system easily.
#### 7.2.4 Understandability and Politeness Requirements 
NFR12  
- The software application of Cyclops Ride Assist will use lanaguge, words, and symbols that are understandable by the global community. 
#### 7.2.5 Accessibility Requirements 
NFR13  
- Cyclops Ride Assist will have signals and cues to alert the user in the case that a user may have some visual or auditory impairment. 
NFR14  
- Cyclops Ride Assist will be able to be mounted to all types of bicycles and tricycles to ensure that as many users can benefit. 

### 7.3 Performance Requirements
#### 7.3.1 Speed and Latency Requirements 
NFR15  
- Cyclops Ride Assist will have a maximum response time of 5 seconds. This is to ensure that the user is able to use Cyclops Ride Assist quickly and get on their way.
NFR16  
- Cyclops Ride Assist will upload the video file to the external storage with a max time of 60 seconds.
NFR17  
- Cyclops Ride Assist will be able to determine an accident within 1s. This is to ensure that the camera will keep the recording of before and after the collision.
NFR18  
- Cyclops Ride Assist can see if a car is nearby to alert the user within 1s with an LED or a vibrational cue. This is to allow the user to have enough time to ensure they are in a safe position. 
NFR19  
- Cyclops Ride Assist will have an alert on its software application to let the user if the storage is low. This is to ensure the system will store in the case of a collision.
NFR20  
- Cyclops Ride Assist will have an alert within 5 seconds of startup on its software application to let the user know if the system components are running out of battery. This is to ensure the system does not crash while in use. 
#### 7.3.2 Safety-Critical Requirements 
NFR21  
- Cyclops Ride Assist will not cause any external damage to the bicycle which could result in loss of safety for the rider. 
NFR22  
- Cyclops Ride Assist will not emit any harmful toxins to the environment. This is to ensure that there is no risk to the environment. 
NFR23  
- Cyclops Ride Assist will have all wiring shielded from human contact. This is to ensure that the user is not negatively affected. 
#### 7.3.3 Precision and Accuracy Requirements 
NFR24  
The precision of Cyclops Road Assist will be to three decimal places. This is to keep as many significant digits to ensure relative precision with other components. 
NFR25    
- The accuracy of Cyclops Road Assist speed reading with be within 1 km/h. This is to ensure that the system is working coherently with the accelerometer subsystem and software application
NFR26  
- The accuracy of Cyclops Road Assist timed camera reading with be within 1 second. This is to ensure that the accuracy of the collision is timed correctly. 
#### 7.3.4 Reliability and Availability Requirements 
NFR27  
- The camera on Cyclops Ride Assist will be able to record once the previous video has finished uploading to storage. This is to ensure that Cyclops can continuously run for the user.
NFR28  
- Cyclops Ride Assist will be able to be used 24 hours per day, 365 days per year. This is to ensure that bikers are covered throughout all times of anyday of any season. 
#### 7.3.5 Robustness or Fault-Tolerance Requirements 
NFR29  
- Cyclops Ride Assist will be able to work consistently even in the case of user drops when in transport. 
#### 7.3.6 Capacity Requirements 
NFR30  
- Cyclops Ride Assist will be able to store multiple 15 second videos in an external storage system. This is to ensure that the user is able to see past videos and continuously record new videos, minimizing downtime. 
#### 7.3.7 Scalability and Extensibility Requirements 
NFR31  
- Cyclops Ride Assist will have extra room in its software and hardware storage to allow for additional components. This is to ensure that Cyclops is scaleable to additional upgrades. 
NFR32  
- Cyclops Ride Assist will be usable to all bicycle users within the next ten years. This is to allow for continuous integration into newer bicycles. 
#### 7.3.8 Longevity Requirements 
NFR33    
- Cyclops Ride Assist will have a lifespan of five years with expected cleaning and maintenance.
### 7.4 Operational and Environmental Requirements
#### 7.4.1 Expected Physical Environment 
NFR34  
 - The expected physical environment will be on a road. Other possible physical environments include trails, sidewalks, pathways.
 NFR35  
 - Cyclops Ride Assist will be used by cyclists in any type of weather. 
 #### 7.4.2 Requirements for Interfacing with Adjacent Systems
NFR36  
- Components of the Cyclops Ride Assist can be interfaced with other software applications and hardware systems such as PCs and adapters. This will include the video storage cards and Cyclops Ride Assist software GUI. 
#### 7.4.3 Productization Requirements 
NFR37  
- Cyclops Ride Assist's hardware and software will be publicly available for use to those interested in furthering the system.
#### 7.4.4 Release Requirements 
NFR38  
- Cyclops Ride Assist will be available as a one-time download and system integration per user.  
### 7.5 Maintainability and Support Requirements
#### 7.5.1 Maintenance Requirements
NFR39  
- Cyclops Ride Assist will have crash logs when the software or hardware fails. This is to allow for the developers to work on a fix for the issue.
NFR40  
- Cyclops Ride Assist will be built in several modules. This is so that components can be removed and replaced when need be. 
#### 7.5.2 Supportability Requirements
NFR41  
- Cyclops Ride Assist will have an instruction manual included to ensure that any common mistakes can be fixed easily by the user.
#### 7.5.3 Adaptability Requirements
NFR42  
- Cyclops Ride Assist's external hardware storage will be able to run under any operating system to view files. 
### 7.6 Security Requirements
#### 7.6.1 Access Requirements
NFR43  
- Cyclops Ride Assist will allow the users to access their videos freely from an external hardware storage drive. This is to allow the user to connect it to various systems. 
#### 7.6.2 Integrity Requirements
N/A
#### 7.6.3 Privacy Requirements
NFR44  
- Cyclops Ride Assist will not store any data in the cloud to protect the user's personal privacy. The data will only be stored in the user's personal external storage.
#### 7.6.4 Audit Requirements
N/A
#### 7.6.1 Immunity Requirements
NFR45  
- Cyclops Ride Assist will be connected per user locally. This is to ensure that there will be no malicious interference from unwanted third-parties.
### 7.7 Cultural and Political Requirements
#### 7.7.1 Cultural Requirements
NFR46  
- Cyclops Ride Assist will have its primary language set as English (Canadian).
NFR47  
- Cyclops Ride Assist will not have any offensive language as to not offend any users. 
### 7.8 Legal Requirements
#### 7.8.1 Compliance Requirements
NFR48  
- Cyclops Ride Assist must follow all safety requirements according to the user's bicycle's standards and requirements. This will include weight and size restrictions to ensure adherance to all types of bicycles.  
#### 7.8.2 Standards Requirements
NFR49  
- Cyclops Ride Assist will comply with all product quality standards for automotive products. This will include all processes between idea generation to customer use and satisfaction.
## 8 Project Issues
### 8.1 Open Issues
1.) Creating accurate documentation for the system specifications.
2.) Starting to develop the software, purchasing some hardware to begin system creation.
### 8.2 Off-the-Shelf Solutions
INNOVV ThirdEYE
- INNOVV ThirdEYE is a blindspot detection system for motorcycles that uses sensors to determine if there are any objects close to the user. It can be either used through a mirror lens or a watch. 
- https://www.innovv.com/innovv-thirdeye
Senzar Motorcycle Sensor
- The Senzar Motorcycle Sensor is another system that uses LEDs, vibration, and radar sensors. 
- https://meetsenzar.com/pages/senzar-m1-motorcycle-bsm
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
