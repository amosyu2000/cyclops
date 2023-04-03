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
  - [2.1. Problem](#21-problem)
  - [2.2. Stakeholders](#22-stakeholders)
  - [2.3. Inputs](#23-inputs)
  - [2.4. Outputs](#24-outputs)
- [3. Goals](#3-goals)
  - [3.1. Reliable Rear Vehicle Detection](#31-reliable-rear-vehicle-detection)
  - [3.2. Convenient Mounting and Dismounting](#32-convenient-mounting-and-dismounting)
  - [3.3. Accurate Crash Identification](#33-accurate-crash-identification)
  - [3.4. Fast Video Buffering and Saving](#34-fast-video-buffering-and-saving)
  - [3.5. Accessible Video and Data Export](#35-accessible-video-and-data-export)
- [4. Stretch Goals](#4-stretch-goals)
  - [4.1. Emergency Response Integration](#41-emergency-response-integration)
  - [4.2. Mobile App](#42-mobile-app)
  - [4.3. Map Integration](#43-map-integration)
- [5. Appendix](#5-appendix)
  - [5.1. Symbolic Parameters](#51-symbolic-parameters)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)
- [Table 5.1.1: List of Symbolic Parameters](#sp)

## List of Figures <!-- omit in toc -->

## 1. Revision History
<div align="center">

<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2022-10-19 | All | Document creation |
| 2022-10-20 | Amos Yu | Improved formatting |
| 2022-11-09 | Aaron Li | Updated content |
| 2023-04-03 | Amos Yu | Updated Problem Statement and Goals for Rev1 |

</div>

## 2. Problem Statement

### 2.1. Problem

As North America pursues greener goals, it is expected a higher percentage of people will adopt cycling as their primary method of transportation as for its relatively low carbon footprint compared to automobiles. However, many roads were not designed and developed with cyclists in mind. Even with dedicated bicycle lanes, cyclists may find themselves in fear as cars, trucks, and buses dart past with a far greater speed and momentum. In the worst cases, accidents may occur leading to both physical injuries and emotional trauma for the cyclist, the automobile driver, their respective families, and the community. Therefore, it is vital that this system will provide greater safety by increasing the awareness of cyclists on the road, allowing drivers and cyclists to share the road responsibly.

This solution to this problem will deliver on the following goals listed in [Section 3](#3-goals).

### 2.2. Stakeholders 

| Stakeholder | Representatives |
|:--|:--|
| Project Proposers | Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos |
| Project Supervisor | Spencer Smith |
| Teaching Assistants | Nicholas Annable, Christopher Schankula, Timofey Tomashevskiy, Samuel Crawford, Ting-Yu Wu |
| End Users | Cyclists |

### 2.3. Inputs

- The user will be able to mount and dismount the system to and from their bicycle. 
- The user will be able to turn the system on and off.
- The user will be able to connect the system to an external power source, such as a power bank.
- The user will be able to save footage at any time during their ride.

### 2.4. Outputs
- The system will stay on the bicycle until manual intervention by the user. 
- The system will be powered on and fully activated with all functionalities. 
- The system will increase the safety and awareness of the cyclist during their ride.
- The system will deliver on the following goals listed in [Section 3](#3-goals). 

## 3. Goals

### 3.1. Reliable Rear Vehicle Detection

The system will be mounted to the bicycle in such a way that it can monitor the blindspots of the cyclist. As soon as the system turns on, it will detect if there are vehicles within MAX_DISTANCE metres of the cyclist's rear. The system will visually notify the cyclist that there is a vehicle in their blindspot without requiring them to turn around and take their eyes off of the road.

### 3.2. Convenient Mounting and Dismounting

The cyclist will be able to mount the system to the bicycle and unmount the system from the bicycle with minimal effort. The system should remain mounted on the bicycle under normal working conditions and in the event of a crash. The should system should only unmount if unmounted by the user or in extreme circumstances of mechanical failure.

### 3.3. Accurate Crash Identification

As soon as the system turns on, it will collect data on the orientation and state of the bicycle. Using the data collected, the system will interpret if the cyclist has been involved in one of many types of accidents (crashing into something, getting hit by something, falling off) with a high degree of accuracy. The crash identification algorithm will consider acceleration due to gravity and a CRASH_THRESHOLD acceleration.

### 3.4. Fast Video Buffering and Saving

As soon as the system turns on, it will collect video footage at a rate of FRAMERATE frames per second. The system will buffer the past BUFFER_TIME seconds of footage and will delete all older footage. In the event of an accident, or if the user hits the capture button, the system will save the buffer footage within MAX_UPLOAD_TIME seconds to an external storage option.

### 3.5. Accessible Video and Data Export

Exported footage and data will be accessible to the user at any point during or after the ride. Taking inspiration from airplane electronic flight recorders, the footage and data exported by the system should clearly communicate to the user the context of the bicycle and its surroundings during each crash or capture. 

## 4. Stretch Goals

### 4.1. Emergency Response Integration

A user will be able to provide the contact information of an emergency contact to the system. The system will alert the saved emergency contact in the event of any serious crashes. 

### 4.2. Mobile App

The user will be able to interface with the system via the mobile app. The user will be able to use the app to set certain parameters and permissions for the system. The system will be able to wirelessly export footage and data to the user's smartphone via the mobile app.

### 4.3. Map Integration

The system will record the distance and places/roads travelled from start to finish of a trip. The system will leverage GPS and real-time traffic data to alert the user of any road closures, accidents, or heavy traffic. 

## 5. Appendix

### 5.1. Symbolic Parameters

<div align="center">

<p id="sp">Table 5.1.1: List of Symbolic Parameters</p>

| Name | Parameter Description | Type | Units |
|:--|:--|:--|:--|
| GRAVITY | Acceleration due to gravity. | float | m/s<sup>2</sup> |
| CRASH_THRESHOLD | The maximum acceleration incurred during a crash. | integer | m/s<sup>2</sup> |
| MAX_DISTANCE | The maximum distance that the rear vehicle detection will monitor. | float | m |
| BUFFER_TIME | The length of footage before the crash that will be saved. | integer | seconds |
| MAX_UPLOAD_TIME | The maximum time required to upload a video to the external storage device. | integer | seconds |
| RESPONSE_RATE | The polling rate at which the output is updated to match the current input. | integer | Hz |
| FRAMERATE | The framerate of the front-facing video | integer | fps |

</div>
