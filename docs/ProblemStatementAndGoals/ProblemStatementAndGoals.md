<div align="center">

<a href="https://github.com/amosyu2000/cyclops">
	<img src="../../refs/header.svg" width="800" height="400" alt="Cyclops header">
</a>

# Problem Statement And Goals <!-- omit in toc -->
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
- [2. Problem Statement](#2-problem-statement)
  - [2.1 Problem](#21-problem)
  - [2.1 Inputs and Outputs](#21-inputs-and-outputs)
  - [2.2 Stakeholders](#22-stakeholders)
- [3. Goals](#3-goals)
  - [3.1. Reliable Blindspot Monitoring](#31-reliable-blindspot-monitoring)
  - [3.2. Convenient Mounting and Dismounting](#32-convenient-mounting-and-dismounting)
  - [3.3. Accurate Crash Detection](#33-accurate-crash-detection)
  - [3.4. Video Buffering and Saving](#34-video-buffering-and-saving)
  - [3.5. Automatic Lighting System](#35-automatic-lighting-system)
- [4. Stretch Goals](#4-stretch-goals)
  - [4.1. Emergency Response Integration](#41-emergency-response-integration)
  - [4.2. Mobile App](#42-mobile-app)
  - [4.3. Map Integration](#43-map-integration)
- [5. Appendix](#5-appendix)
  - [5.1. Symbolic Parameters](#51-symbolic-parameters)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)
- [Table 5.1.1: List of Symbolic Parameters](#sb)

## List of Figures <!-- omit in toc -->

## 1. Revision History
<div align="center">

<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2022-10-19 | All | Document creation |
| 2022-10-20 | Amos Yu | Improved formatting |
| 2022-11-09 | Aaron Li | Updated document |

</div>

## 2. Problem Statement

### 2.1 Problem

As North America pursues greener goals, it is expected a higher percentage of people will adopt cycling as their primary method of transportation as for its relatively low carbon footprint compared to automobiles. However, many roads were not designed and developed with cyclists in mind. Even with dedicated bicycle lanes, cyclists may find themselves in fear as cars, trucks, and buses dart past with a far greater speed and momentum. In the worst cases, accidents may occur leading to both physical injuries and emotional trauma for the cyclist, the automobile driver, their respective families, and the community. Therefore, it is vital that this system will be used to increase the safety of the road, allowing drivers and cyclists to share the road responsibly.  
This project will deliver on the following goals listed in Section 3.  

### 2.1 Inputs and Outputs
The inputs will be as follows: 
- The user will be able to mount system onto their own personal bicycle. 

The outputs will be as follows:
- The system will stay on the bicycle until manual intervention by the user. 
- The system will be powered on and fully activated with all functionalities. 
- The system will be able to provide the following goals as outlined in Section 3 - Goals. 
- The user will have a safe experience travelling from their start to their destination. 

### 2.2 Stakeholders 
The stakeholders in this project are as follows:
  - Cyclists: These will be the main users of this system. 
  - Automotive vehicle users: These users are also involved in ensuring the safety of all on the road. 
  - The development team of Cyclops: These will be the primary developers of the Cyclops Ride Assist project. 
## 3. Goals

### 3.1. Reliable Blindspot Monitoring
As long as it is mounted to the bicycle, the system will detect if there are objects in the cyclist's blindspots. The system will notify the cyclist that there is an object in their blindspot without requiring them to take their eyes off of the road.

### 3.2. Convenient Mounting and Dismounting
The cyclist will be able to mount the system to the bicycle and unmount the system from the bicycle with minimal effort. When mounted, the system will be secure and will not unmount except if unmounted by the cyclist or under extreme circumstances.

### 3.3. Accurate Crash Detection
As long as it is mounted on the bicycle, the system will collect data on the movement of the bicycle. The system will interpret if the cyclist has been involved in one of many types of accidents (crashing into something, getting hit by something, falling off) with a high degree of accuracy. 

### 3.4. Video Buffering and Saving
As long as it is mounted on the bicycle, the system will collect video footage. The system will buffer the past BUFFER_TIME_MINUTES minutes of footage and will delete all older footage. In the event of an accident, the system will save the buffer footage. The user will be able to access saved footage.

### 3.5. Automatic Lighting System 
The user will be able to turn on and off the headlamp. When turned on, the headlamp will illuminate the path in front of the bicycle in low-light conditions. When turned on, the headlamp will not decrease the quality of the video footage. Furthermore, the light will be able to detect any changes in lighting and turn itself on or off automatically. 

## 4. Stretch Goals

### 4.1. Emergency Response Integration
Call saved Emergency Contact for the user in the case of any accidents. 

### 4.2. Mobile App
The user will be able to interface with the system via the mobile app. The user will be able to use the app to set certain parameters for the system. The system will be able to transfer save footage to the user's smartphone via the mobile app.

### 4.3. Map Integration
Record the distance and places/roads travelled from start to finish on the mobile app. GPS Detection to alert the User of any road closures, accidents, heavy traffic. 

## 5. Appendix

### 5.1. Symbolic Parameters

<div align="center">

<p id="sp">Table 5.1.1: List of Symbolic Parameters</p>

| Parameter | Description |
|:--|:--|
| BUFFER_TIME_MINUTES | The length of footage that will be saved after an accident occurs (in minutes). |

</div>
