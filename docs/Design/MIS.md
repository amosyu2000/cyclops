<div align="center">

<a href="https://github.com/amosyu2000/cyclops">
	<img src="../../refs/header.svg" width="800" height="400" alt="Cyclops header">
</a>

# Module Interface Specification <!-- omit in toc -->
Cyclops Ride Assist: Real-time bicycle crash detection and blindspot monitoring.<br/>  
__Team 9__  
Aaron Li (lia79)  
Amos Cheung (cheuny2)  
Amos Yu (yua25)  
Brian Le (leb7)  
Manny Lemos (lemosm1)  

</div>

<div style="page-break-after: always;"></div> <!-- Page Break -->

## Table Of Contents <!-- omit in toc -->
- [1. Revision History](#1-revision-history)
- [2. Introduction](#2-introduction)
- [3. Purpose](#3-purpose)
- [4. Scope](#4-scope)
	- [4.1. System Context](#41-system-context)
- [5. Project Overview](#5-project-overview)
- [6. System Variables](#6-system-variables)
- [7. User Interfaces](#7-user-interfaces)
	- [7.1. Buttons](#71-buttons)
- [8. Mechanical Hardware](#8-mechanical-hardware)
	- [8.1. Raspberry Pi Mechanical Specifications](#81-raspberry-pi-mechanical-specifications)
	- [8.2. Polylactic Acid (PLA) Material](#82-polylactic-acid-pla-material)
- [9. Electrical Components](#9-electrical-components)
	- [9.1. Raspberry Pi Electrical Specifications](#91-raspberry-pi-electrical-specifications)
	- [9.2. Resistor Specifications](#92-resistor-specifications)
	- [9.3. Breadboard Specifications](#93-breadboard-specifications)
- [10. Communication Protocols](#10-communication-protocols)
	- [10.1. USB Protocol](#101-usb-protocol)
- [11. Software Modules](#11-software-modules)
	- [11.1. video\_buffer.py](#111-video_bufferpy)
		- [11.1.1. Module Implementation](#1111-module-implementation)
		- [11.1.2. Module Secrets](#1112-module-secrets)
		- [11.1.3. Module Relationships](#1113-module-relationships)
		- [11.1.4. Likely Changes](#1114-likely-changes)
		- [11.1.5. Unlikely Changes](#1115-unlikely-changes)
- [12. Timeline](#12-timeline)
- [13. Appendix](#13-appendix)
	- [13.1. Reflection](#131-reflection)
		- [13.1.1. Solution Limitations](#1311-solution-limitations)
	- [13.2. References](#132-references)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)

## List of Figures <!-- omit in toc -->
- [Figure 4.1.1: CRA System Context Diagram](#scd)
- [Figure 5.1: CRA Functional Decomposition Diagram](#fdd)

## 1. Revision History
<div align="center">

<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| 2023-01-17 | Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos | Document created |

</div>

## 2. Introduction
This document is the Modular Interface Specification of Cyclops Ride Assist (CRA) system. The purpose of this document is to outline the design specification for each component in CRA and serve as the basis for implementation work when building the system. 

## 3. Purpose
The purpose of this project is to create a system that helps cyclists to have a more secured experience especially on roads without bike lanes.

Cyclops Ride Assist (CRA) is going to be an all-in-one, easily mountable, and quick to setup system that adds modern car safety features onto a bike, such as blind spot detection and crash detection. The system will also have a built in headlamp that will illuminate during night time, not just for the cyclist to see but also for cars around to realize the bike.

## 4. Scope
CRA is going to be a bike assist system with convenient mounting, accurate crash detection, video buffering and saving, reliable blindspot monitoring and a user controlled headlamp that helps cyclist to have a peace of mind while riding on the road. Although CRA is primarily targeted towards road cyclists, it will able be useful for cyclists who ride on mountains or trails.

### 4.1. System Context

<div align="center">
<p id="scd">Figure 4.1.1: CRA System Context Diagram</p>

![image](https://user-images.githubusercontent.com/68861121/193955661-d965823f-079b-444f-9cb3-cf34a120ac87.png)  

</div>

## 5. Project Overview

<div align="center">
<p id="fdd">Figure 5.1: CRA Functional Decomposition Diagram</p>

![image](https://user-images.githubusercontent.com/46848538/194148017-fdbf2709-8ab7-48b0-b066-e4e0d635e83c.png)  

</div>

## 6. System Variables

## 7. User Interfaces
### 7.1. Buttons

Reference: 
## 8. Mechanical Hardware

### 8.1. Raspberry Pi Mechanical Specifications   

<div align="center">
<p id="fdd">Figure 8.1: Raspberry Pi Mechanical Drawing and Schematic</p>

![image](https://user-images.githubusercontent.com/58313755/213242698-29e0ad61-2088-429e-91e5-0e97043f7a81.png)  

</div>
The mechanical specifications of the Raspberry Pi is as follows:

| Part | Specification |   
|:--|:--|   
| INSERT | SPEC |   
| INSERT | SPEC |   
| INSERT | SPEC |   

### 8.2. Polylactic Acid (PLA) Material

The mechanical chassis and frame will be created using Polylactic Acid (PLA) filament, molded through a Prusa i3 MK3s 3D printer. 

The mechanical specifications of PLA are as follows:
| Part | Specification |   
|:--|:--|   
| PLA | Brian Le |   
| 2022-09-23 | Brian Le |   
| 2022-10-20 | Amos Yu |    


## 9. Electrical Components

### 9.1. Raspberry Pi Electrical Specifications 
<div align="center">
<p id="fdd">Figure 8.1: Raspberry Pi Electrical Schematic</p>

![image](https://user-images.githubusercontent.com/58313755/213247210-1cf36f4d-d1d2-463e-be8d-ee6f19534f09.png)  

</div>


### 9.2. Resistor Specifications

| Part | Specification |   
|:--|:--|   
| INSERT | SPEC |   
| INSERT | SPEC |   
| INSERT | SPEC |   

Reference:

### 9.3. Breadboard Specifications

| Part | Specification |   
|:--|:--|   
| INSERT | SPEC |   
| INSERT | SPEC |   
| INSERT | SPEC |   

## 10. Communication Protocols

### 10.1. USB Protocol

Reference: 


## 11. Software Modules
### 11.1. video_buffer.py
#### 11.1.1. Module Implementation
Composed of a class Buffer. Provides the functionality of starting, stopping, and logging a video clip. 
#### 11.1.2. Module Secrets
- Video capture instance.
- Frames of video clips.
- Video codec.
#### 11.1.3. Module Relationships
- Receives the following Buffer class instantiation parameters from __main__.py
  - video_length : integer
  - num_partitions : integer
  - fps : integer
  - save_directory : string
  - temp_directory : string
  - camera_id : integer
  - resolution : integer
#### 11.1.4. Likely Changes
- Reduce the number of input parameters to the instantiation of the Buffer class. These inputs will be replaced by fixed parameters which are deemed most suitable.
#### 11.1.5. Unlikely Changes
- Change the camera being used from a USB web-camera to the Raspberry Pi Camera Module.
  - Subsequently, a large portion of the code for the Buffer class will have to be rewritten.
## 12. Timeline
| Date | Task                                                                                                    | Person                | Testing                                                                                                                                                                          |
|-------------------|---------------------------------------------------------------------------------------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 2023-01-22        | Creation of crash detection algorithm.                                                                  | Manny Lemos, Amos Yu  | Automated testing to determine response under a wide range of accelerometer inputs.                                                                                              |
| 2023-01-25        | Update design and 3D print hardware case to accommodate the camera, battery pack, and mounting bracket. | Aaron Li, Amos Cheung | Manual testing. Ensure everything fits as expected.                                                                                                                              |
| 2023-01-28        | Design and 3D print a mounting bracket to attach the hardware case to bicycle fork.                     | Aaron Li, Manny Lemos | Manual testing. Ensure the mounting bracket can support the weight of the loaded hardware case sufficiently. Ensure the mounting bracket will function for common bicycle forks. |
| 2023-01-31        | Swap breadboard and jumper wires for PCB and soldered connections.                                      | Amos Cheung           | Manual testing. Verify connections using multimeter.                                                                                                                             |
| 2023-02-05        | Integration of all software modules.                                                                    | Brian Le, Amos Yu     | Manual Testing. Mount the hardware to the bicycle and ensure it functions as detailed in the SRS Document.           

## 13. Appendix

### 13.1. Reflection
Cyclops ride assist aims to fill the ride monitoring and crash avoidance gap in the cycling market. This solution takes the form of a camera, accelerometer, and distance sensor. These inputs are parsed by an embedded computer to provide users with warning lights when vehicles are approaching, and an automatically logged clip if a crash is detected.
#### 13.1.1. Solution Limitations
**Camera Resolution:** The maximum camera resolution possible with the current implementation is 640p. This is due to the data transfer speeds being limited by the USB connection made between the camera and the Raspberry Pi. Using the Raspberry Camera Module is an alternative to the current implementation which would overcome the USB bandwidth issue and could increase the resolution to 1080p. This alternative comes with the downside of addition cost and recording software rewriting because the Pi Camera Module uses custom libraries.<br>
**Camera Position:** With the current implementation the camera is seated atop the bicycle forks facing forward. This provides video capture of the volume of space in front of the cyclist. The limitation of this implementation is evident, there is no camera footage of the volume of space behind the rider. An alternative to the current state would be to add an additional camera with a view behind the cyclist. However, due to the current USB bandwidth issues with a single camera and the lack of support for dual Raspberry Pi Camera Modules this change is not feasible. A possible alternative would be changing the position of the current camera to face being the cyclist.<br>
**Battery Life:** For cyclists who go on multi hour long bicycle rides, battery life may be of concern. The Raspberry Pi used to perform computations is not particularly battery efficient compared to more project specific embedded computers who do not have as much computational overhead. The capacity of the current battery pack being used is 10,000mah. To improve battery life, a higher capacity battery pack could be purchased. However, a higher capacity battery pack is almost certain to come along with the unwanted side effects of a larger size and heavier weight. 
 ### 13.2. References

[1] "Raspberry Pi 4 Mechanical Drawing", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-mechanical-drawing.pdf

[2] "What is PLA?", 2023. [Online]. Available: https://www.twi-global.com/technical-knowledge/faqs/what-is-pla

[3] "Raspberry Pi 4 Electrical Schematic", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf