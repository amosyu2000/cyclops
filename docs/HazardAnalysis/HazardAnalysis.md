<h1 align="center">Hazard Analysis</h1> <!-- omit in toc -->
<p align="center">
	Cyclops Ride Assist: Real-time bicycle crash detection and blindspot monitoring.<br/>
	<b>Team 9</b><br/>
	Aaron Li (lia79)<br/>
	Amos Cheung (cheuny2)<br/>
	Amos Yu (yua25)<br/>
	Brian Le (leb7)<br/>
	Manny Lemos (lemosm1)<br/>
</p> 

## Table Of Contents <!-- omit in toc -->
- [1. Revision History](#1-revision-history)
- [2. Introduction](#2-introduction)
- [3. Scope and Purpose](#3-scope-and-purpose)
- [4. Definition of Hazard](#4-definition-of-hazard)
- [5. Critical Assumptions](#5-critical-assumptions)
- [6. System Boundary](#6-system-boundary)
	- [6.1. Front Facing Camera with Storage](#61-front-facing-camera-with-storage)
	- [6.2. Crash Detection Sensors](#62-crash-detection-sensors)
	- [6.3. Rear-Left Facing Camera with Storage](#63-rear-left-facing-camera-with-storage)
	- [6.4. Microcontroller](#64-microcontroller)
	- [6.5. Crash Detection Software](#65-crash-detection-software)
	- [6.6. Crash Detection Software](#66-crash-detection-software)
	- [6.7. Blindspot Detection Software](#67-blindspot-detection-software)
	- [6.8. Box and Mount](#68-box-and-mount)
	- [6.9. Lightswitch](#69-lightswitch)
	- [6.10. Light](#610-light)
- [7. Failure Modes and Effect Analysis](#7-failure-modes-and-effect-analysis)
	- [7.1. Hazards Out of Scope](#71-hazards-out-of-scope)
	- [7.2. Failure Modes and Effect Analysis Table](#72-failure-modes-and-effect-analysis-table)
- [8. Safety and Security Requirements](#8-safety-and-security-requirements)
	- [8.1. Safety Requirements](#81-safety-requirements)
	- [8.2. Access Requirements](#82-access-requirements)
	- [8.3. Integrity Requirements](#83-integrity-requirements)
	- [8.4. Privacy Requirements](#84-privacy-requirements)
- [9. Roadmap](#9-roadmap)
- [10. Appendix](#10-appendix)

## List of Figures <!-- omit in toc -->
## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)
- [Table 7.2.1: Failure Modes and Effect Analysis](#fmea)

## 1. Revision History
<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2022-10-19 | Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos | Document created |

## 2. Introduction

## 3. Scope and Purpose
This document identifies potential hazards which arise due to failures in the hardware and software used in the Cyclops Ride Assist system, the causes and effects of these failures, plans for hazard mitigation, and the safety and security requirements which emerge as a result of this knowledge.

## 4. Definition of Hazard
A hazard is any property of the CRA system that has the potential to cause harm in both the user and the various systems that make up CRA. In CRA, there are hazards in safety (video logging, vehicle detection) and physical (mount, enclosure). 

## 5. Critical Assumptions
There are no critical assumptions that were made. 
## 6. System Boundary
The Cyclops Ride Assist system is composed of the following.

### 6.1. Front Facing Camera with Storage
### 6.2. Crash Detection Sensors
### 6.3. Rear-Left Facing Camera with Storage
### 6.4. Microcontroller
### 6.5. Crash Detection Software
### 6.6. Crash Detection Software
### 6.7. Blindspot Detection Software
### 6.8. Box and Mount
### 6.9. Lightswitch
### 6.10. Light

## 7. Failure Modes and Effect Analysis
### 7.1. Hazards Out of Scope
### 7.2. Failure Modes and Effect Analysis Table
<p id="fmea">Table 7.2.1: Failure Modes and Effect Analysis</p>

| Design Function | Ref # | Failure Mode | Effects of Failures | Causes of Failure | Recommended Action | SR |
|:--|:--|:--|:--|:--|:--|:--|
Crash Detection		| H1-1		| False negative crash detection. | The current loop of video will not be logged to the storage device. | a. Sensor failure (bias, drift, complete failure, precision degradation). <br/> b. Crash was not violent enough to trigger a crash detection sequence.\end{tabular | a. Perform a sensor calibration and test when the system is turned on. Indicate an issue if one is detected. <br/> b. Allow users to force video loop logging with a  button. | a. SR-1 <br/> b. AR-1|
| | H1-2 | False positive crash detection. | An unnecessary loop of video will be logged to the storage device. | a. Sensor failure (bias, drift, complete failure, precision degradation). <br/> b. A non-crash event had trademark features of a crash (e.g. high g forces, tipping). | a. Same as H1-1a <br/> b. Allow user to cancel video loop logging with a button. | a. SR-1 <br/> b. AR-1 |
Video Logging | H2-1 | Storage device cannot accommodate the loop of video attempting to be logged.	| Video loop will not be logged to the storage device. | a. Video loop is too large to be logged on the storage device. | a. Log the most recent half of the current video loop, and halve the length of the video loop going forward. When sufficient storage is available on the storage device, standard video loop length should be reinstated. 
| a.SR-3 | H2-2 | Front/Rear facing camera. | Camera footage will be void or non-optimal in the event of a camera loop logging. | a. Debris obstructs the camera's view. <br/> b. Complete camera or camera feed failure. | a. Place the camera in a position unlikely to be impacted by debris (eg. not on underside of downtube) <br/> b. Perform a camera feed check when the system is turned on. Indicate an issue if one is detected. | a. IR-1 <br/> b. SR-1 |
| Blind Spot Detection | H3-1 | False negative blind spot detection. | A vehicle exists in the users blind spot, but they are not alerted. | a. The vehicle is not recognized by the computer vision program. <br/> b. The rear facing camera is obstructed by debris. <br/> c. The rear facing camera or camera feed fails. | a. Provide a separate lesser warning for non-vehicles that are detected in the users blind spot. <br/> b. Same as H2-2a <br/> c. Same as H2-2b | a. SR-4 <br/> b. SR-1 <br/> c. SR-1 |
| | H3-2 | False positive blind spot detection. | A user is alerted that a vehicle exists in their blindspot when no vehicle is present | a. Debris obstructs the rear facing camera's view. | a. Same as H2-2a | a. SR-1 |
| Housing to protect hardware. | H4-1 | Housing integrity is violated. | Internal hardware components  are damaged or destroyed. | a. Housing is submerged in water (e.g. rain, puddle lake). <br/> b. Housing is violently rattled. <br/> c. Housing is dropped to the ground. | a. Make housing waterproof <br/> b. Protect the microcontroller from vibrations using damping. <br/> c. Make the housing robust and resistant to damage do to shock. | a. IR-1 <br/> b. SR-2, IR-1 <br/> b. SR-2 |
| Mount housing to bicycle. | H5-1 | Mount failure. | Housing is dropped to the ground. | a. Mount is impacted by debris. <br/> b. Rattling loosens mount grip. | a. Place mount in a position unlikely to be impacted by debris (eg. not on underside of downtube) <br/> b. Instruct user to firmly tighten the mount to their bicycle. Line the gripping portion of the mount with rubber. | a. SR-2, IR-1 <br/> b. SR-2, IR-1 |

## 8. Safety and Security Requirements

### 8.1. Safety Requirements

| SR-1 |  A system welfare check will be conducted each time the CRA is powered on to verify that all cameras and sensors are successfully communicating with the microcontroller. |  
|:--|:--|  
| Rationale |A problem with the rear facing camera could result in unexpected blind spot detection behaviour (false positives or false negatives). A problem with the front or rear facing camera could result in footage of a crash being lost. A problem with crash detection sensors could result in unexpected crash detection behaviour (false positives or false negatives).|  
| Associated Hazards |  H1-1a, H1-2a, H2-2b, H3-1b, H3-1c, H3-2a |  

| SR-2 |  Safety instructions will be created to ensure that the CRA is properly equipped and mounted for the user.  |  
|:--|:--|  
| Rationale | Instructions will allow the user to properly mount and maintain their system.|  
| Associated Hazards |  H4-1a, H4-1b, H5-1a, H5-1b |  

| SR-3 |  The storage device will be checked on startup by the system to ensure there is enough storage to hold two videos and will alert the user if the space is insufficient. |  
|:--|:--|  
| Rationale | In the case that the storage memory device is full, videos will be cut short to ensure that the user has the footage of the latest accident that they have been involved in. |  
| Associated Hazards |  H2-1a |  

| SR-4 |  The CV Vision will be checked on startup by the system to ensure that all required apps, images can still be accessed and used |  
|:--|:--|  
| Rationale | This is to ensure that the cameras are able to differentiate between vehicles and other objects |  
| Associated Hazards |  H3-1a |  
### 8.2. Access Requirements
| AR-1 |  CRA will allow the users to access their videos freely from an external hardware storage drive. |  
|:--|:--|  
| Rationale | This is to allow the user to connect it to their own personal systems to view, delete their videos. There is no need for encryption as this would complicate the process. |  
| Associated Hazards |  N/A |  
### 8.3. Integrity Requirements
| IR-1 |  The mounting system will be made with solid and sustainable material to ensure mechanical integrity. |  
|:--|:--|  
| Rationale | This will be able to withstand changes in weather and temperature, accidental drops, and debris. |  
| Associated Hazards |  H2-2a, H4-1a, H4-1b, H5-1a, H5-1b |  

### 8.4. Privacy Requirements
| PR-1 |  CRA will not be connected to the internet but will be used and trained locally for CV purposes. |  
|:--|:--|  
| Rationale | This is to ensure that the footage of accidents will not be posted on the internet without the consent of the user. Instead all footage will be saved to an external hardware storage device. |   
| Associated Hazards |  N/A |  
## 9. Roadmap
The roadmap of CRA is a projection of the safety and security requirements listed above. The majority of these requirements will be implemented on the initial prototype and final application due to the nature of the system and its functionalities. Requirements will be constantly reevaluated with several factors in consideration such as time and project constraints. Towards the end of the project, the hazard analysis will be an evaluation over the project to get an understanding of what risks have been successfully mitigated and which ones will still require work.


## 10. Appendix