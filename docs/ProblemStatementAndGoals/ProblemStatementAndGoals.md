<h1 align="center">Problem Statement and Goals</h1> <!-- omit in toc -->
<p align="center">
	Cyclops Ride Assist: Real-time bicycle crash detection and blindspot monitoring.<br/>
	<b>Team 9</b><br/>
	Aaron Li (lia79)<br/>
	Amos Cheung (cheuny2)<br/>
	Amos Yu (yua25)<br/>
	Brian Le (leb7)<br/>
	Manny Lemos (lemosm1)<br/>
</p> 

## Table of Contents <!-- omit in toc -->
- [1. Revision History](#1-revision-history)
- [2. Problem Statement](#2-problem-statement)
- [3. Goals](#3-goals)
  - [3.1. Reliable Blindspot Monitoring](#31-reliable-blindspot-monitoring)
  - [3.2. Convenient Mounting and Dismounting](#32-convenient-mounting-and-dismounting)
  - [3.3. Accurate Crash Detection](#33-accurate-crash-detection)
  - [3.4. Video Buffering and Saving](#34-video-buffering-and-saving)
  - [3.5. Headlamp](#35-headlamp)
- [4. Stretch Goals](#4-stretch-goals)
  - [4.1. Emergency Response Integration](#41-emergency-response-integration)
  - [4.2. Mobile App](#42-mobile-app)
  - [4.3. Map Integration](#43-map-integration)
- [5. Appendix](#5-appendix)
  - [5.1. Symbolic Parameters](#51-symbolic-parameters)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)

## 1. Revision History
<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2022-10-19 | All | Document creation |

## 2. Problem Statement
Cycling is an economic mode of transportation which has an extremely low carbon footprint. As North America pursues greener goals, it is expected that more people will adopt cycling as their primary method of transportation. However, many North American roads were not designed with cyclists in mind; some roads do not have any bike lanes to speak of, and many of those that do are nothing more than additional paint on an already narrow lane-way. Naturally, a combined road where multi-ton vehicles are speeding past cyclists is a recipe for disaster. When vehicles impact cyclists, the mismatch in size and mass may result in a cyclist's serious injury or even death. Evidently, any means to improve the safety of cyclists before, during, and after a crash is of vital importance to all who share the road, and more specifically those who travel by bicycle.

## 3. Goals

### 3.1. Reliable Blindspot Monitoring
As long as it is mounted to the bicycle, the system will detect if there are objects in the cyclist's blindspots. The system will notify the cyclist that there is an object in their blindspot without requiring them to take their eyes off of the road.

### 3.2. Convenient Mounting and Dismounting
The cyclist will be able to mount the system to the bicycle and unmount the system from the bicycle with minimal effort. When mounted, the system will be secure and will not unmount except if unmounted by the cyclist or under extreme circumstances.

### 3.3. Accurate Crash Detection
As long as it is mounted on the bicycle, the system will collect data on the movement of the bicycle. The system will interpret if the cyclist has been involved in one of many types of accidents (crashing into something, getting hit by something, falling off) with a high degree of accuracy. 

### 3.4. Video Buffering and Saving
As long as it is mounted on the bicycle, the system will collect video footage. The system will buffer the past BUFFER_TIME_MINUTES minutes of footage and will delete all older footage. In the event of an accident, the system will save the buffer footage. The user will be able to access saved footage.

### 3.5. Headlamp
The user will be able to turn on and off the headlamp.When turned on, the headlamp will illuminate the path in front of the bicycle in low-light conditions. When turned on, the headlamp will not decrease the quality of the video footage.

## 4. Stretch Goals

### 4.1. Emergency Response Integration
Call saved Emergency Contact for the user in the case of any accidents. 

### 4.2. Mobile App
The user will be able to interface with the system via the mobile app. The user will be able to use the app to set certain parameters for the system. The system will be able to transfer save footage to the user's smartphone via the mobile app.

### 4.3. Map Integration
Record the distance and places/roads travelled from start to finish on the mobile app. GPS Detection to alert the User of any road closures, accidents, heavy traffic. 

## 5. Appendix

### 5.1. Symbolic Parameters
BUFFER_TIME_MINUTES - The length of footage that will be saved after an accident occurs (in minutes). 
