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

## 3. Purpose

## 4. Scope

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

### 6.1 Monitored and Controlled Variables

The following are a list of variables that are to be monitored.

| Monitor Var | Monitor Type | Range | Units | Comments |
|:--|:--|:--|:--|:--|
distance_cm | Distance | [0, 10000] | cm | Distance to closest obstacle |
| curr_frames | Frequency | [0, 30] | FPS | The rate at which the video buffer can sample a frame for video feed |
| run_buffer | Boolean | N/A | N/A | Boolean of if the buffer should run or not
| average_of | Acceleration | [-16, 16] | G's | Takes a rolling average of the xyz acceleration points | 
| avg_x | Acceleration | N/A | m/s<sup>2</sup> | Acceleration in the x plane |
| avg_y | Acceleration | N/A | m/s<sup>2</sup> | Acceleration in the y plane |
| avg_z | Acceleration | N/A | m/s<sup>2</sup> | Acceleration in the z plane |
| avg_norm | Acceleration | N/A | m/s<sup>2</sup> | Normal of the accelerations |

The following are a list of variables that are to be controlled.

| Monitor Var | Controlled Type | Range | Units | Comments |
|:--|:--|:--|:--|:--|
| lock | Mutex | N/A | N/A | Mutex |
| data_points | Size | TBD | N/A | Maximum number of data points to show on the plot and kept track of | 
| GPIO | Boolean | N/A | N/A | Toggle for LEDs to display sensor data
| frame_width | Soze | [640, 1920] | px | Capture resolution |
| frame_height | Size | [480, 1080] | px | Capture resolution |
| video_length | Time | [0 - 60] | Seconds | The length in seconds of the requested video |

### 6.2 Contants

| Constant Var | Constant Type | Value | Units | Comments |
|:--|:--|:--|:--|:--|


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
- 
#### 11.1.5. Unlikely Changes
- change the video clipping implementation such that 

## 12. Timeline

## 13. Appendix

### 13.1. Reflection

#### 13.1.1. Solution Limitations

### 13.2. References

[1] "Raspberry Pi 4 Mechanical Drawing", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-mechanical-drawing.pdf

[2] "What is PLA?", 2023. [Online]. Available: https://www.twi-global.com/technical-knowledge/faqs/what-is-pla

[3] "Raspberry Pi 4 Electrical Schematic", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf