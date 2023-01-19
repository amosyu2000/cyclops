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
	- [8.3. Mechanical Design](#83-mechanical-design)
- [9. Electrical Components](#9-electrical-components)
	- [9.1. CRA Electrical Specifications](#91-cra-electrical-specifications)
	- [9.2. Raspberry Pi Electrical Specifications](#92-raspberry-pi-electrical-specifications)
	- [9.3. Printed Circuit Board (PCB) Specifications](#93-printed-circuit-board-pcb-specifications)
	- [9.4. Resistor Specifications](#94-resistor-specifications)
- [10. Communication Protocols](#10-communication-protocols)
	- [10.1. USB Protocol](#101-usb-protocol)
	- [10.2. Wi-Fi Protocol](#102-wi-fi-protocol)
- [11. Software Modules](#11-software-modules)
	- [11.1. video\_buffer.py](#111-video_bufferpy)
	- [11.2. acceleration\_plot.py](#112-acceleration_plotpy)
	- [11.3. (MODULE NAME).py](#113-module-namepy)
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
- [Figure 8.1.1: Raspberry Pi 4 Model B Physical Schematic](#rpps)
- [Figure 8.3.1: Mechanical Housing Drawing Top](#mdht)
- [Figure 8.3.2: Mechanical Housing Drawing Bottom](#mhdb)
- [Figure 9.1.1: CRA Circuit Diagram](#ccd)
- [Figure 9.1.2: CRA Breadboard Schematic](#cbs)
- [Figure 9.2.1: Raspberry Pi 4 Model B Circuit Diagram](#rpies)
- [Figure 11.0.1: CRA Software Stack](#css)

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

![image](https://user-images.githubusercontent.com/46848538/213323907-9c962406-62c2-4108-8010-261398c026c2.png)  

</div>

## 5. Project Overview

<div align="center">
<p id="fdd">Figure 5.1: CRA Functional Decomposition Diagram</p>

![image](https://user-images.githubusercontent.com/46848538/213323584-7ad14da3-8865-4878-8e06-ba42eb49f347.png)  

</div>

## 6. System Variables

### 6.1. Monitored and Controlled Variables

The following are a list of variables that are to be monitored.

| Monitor Var | Monitor Type | Range | Units | Comments |
|:--|:--|:--|:--|:--|
distance_cm | Distance | [0, 4000] | cm | Distance to closest obstacle |
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

### 6.2. Contants

| Constant Var | Constant Type | Value | Units | Comments |
|:--|:--|:--|:--|:--|


## 7. User Interfaces

### 7.1. Inputs

| Input Name | Input Type | Range | Units | Comments |
|:--|:--|:--|:--|:--|
| Power Button | Physical | [0, 1] | N/A | Button that is used to power on the system and automatically run the blindspot/crash detection scripts |
| Mount | Physical | N/A | N/A | Mount used to secure Cyclops to the bike |


### 7.2. Outputs

| Output Name | Output Type | Range | Units | Comments |
|:--|:--|:--|:--|:--|
| LEDS | Visual | [0, 5] | N/A | 5 LEDS are used to indicate the distance of an object in your blindspot as well as to signify that the cyclops is on an running |
| SD | Physical | N/A | N/A | SD slot is used to store the video buffer when a crash has been detected |

Reference: 
## 8. Mechanical Hardware

### 8.1. Raspberry Pi Mechanical Specifications   

<div align="center">
<p id="rpimd">Figure 8.1.1: Raspberry Pi Mechanical Drawing and Schematic [1]</p>

![image](https://user-images.githubusercontent.com/58313755/213242698-29e0ad61-2088-429e-91e5-0e97043f7a81.png)  

</div>
The Raspberry Pi 4 Model B is the microcomputer that will be used for all software and processing. The mechanical specifications of the Raspberry Pi is as follows:

| Raspberry Pi Mechanical Specifications | Value |   
|:--|:--|   
| Dimensions |  85mm x 56mm | 
| CPU | Quad core Cortex-A72 (ARM V8) | 
| Ports | USB3, USB2, USB-C, HDMI, MicroSD |   
| RAM | 4GB |   
| Operating Temperature | 0-50C |   
| Audio | 4-Pole Stereo Audio |   
| Video | Composite Video |   

### 8.2. Polylactic Acid (PLA) Material

The mechanical chassis and frame will be created using Polylactic Acid (PLA) filament, molded through a Prusa i3 MK3s 3D printer. 

The color of the PLA material was chosen to be white in order to reflect the NFRs outlined in the SRS document, specifically CNFR1. 

The mechanical specifications of PLA are as follows [2]:

| PLA Specifications | Value |   
|:--|:--|   
| Heat Deflection Temperature | 52C |   
| Density | 1.24 g/cm3 |   
| Tensile Strength | 50MPa |    

### 8.3. Mechanical Design

The mechanical chassis and frame is shown below in Figure 8.3. Each module outlined in the above sections will be fitted with a frame or mount to allow for ease-of-use and protection. 

The mechanical design was created using PLA and the Prusa i3 MK3s 3D printer. 
<div align="center">
<p id="mhdt">Figure 8.3.1: Mechanical Housing Drawing Top</p>

![image](https://user-images.githubusercontent.com/58313755/213313607-af71d40e-9ca5-408c-966d-48411e60234f.png)  

</div>

| Mechanical Frame Top Component Specification | Value |   
|:--|:--|   
| Dimensions | 91.25mm x 60mm x 19mm |   
| Weight | 23grams | 
| Material | PLA | 

<div align="center">
<p id="mhdb">Figure 8.3.2: Mechanical Housing Drawing Bottom</p>

![image](https://user-images.githubusercontent.com/58313755/213313743-9a756f6c-f0cb-4c9f-b2b1-f3c17105ddc7.png)  

</div>

| Mechanical Frame Bottom Component Specification | Value |   
|:--|:--|   
| Outer Dimensions | 91.25mm x 60mm x 6mm |   
| Weight | 15 grams |   
| Material | PLA |   


## 9. Electrical Components


### 9.1. CRA Electrical Specifications

<div align="center">
<p id="ccd">Figure 9.1.1: CRA Circuit Diagram</p>

![image](https://user-images.githubusercontent.com/46848538/213303316-aaa5c7b9-9049-4c29-99ec-831ef7829bec.png)

<p id="cbs">Figure 9.1.2: CRA Breadboard Schematic</p>

![image](https://user-images.githubusercontent.com/46848538/213303319-a90aff03-9621-4622-940e-068fe115fd24.png)

</div>

### 9.2. Raspberry Pi Electrical Specifications

The Raspberry Pi 4's reduced electrical schematic can be seen below. Using various pins and ports provided, CRA will be able to accomplish what is set out in the scope. 
<div align="center">
<p id="rpies">Figure 9.2.1: Raspberry Pi Circuit Diagram [3]</p>

![image](https://user-images.githubusercontent.com/58313755/213247210-1cf36f4d-d1d2-463e-be8d-ee6f19534f09.png)  

</div>

| Raspberry Pi Electrical Specifications | Value |   
|:--|:--|   
| Microchip | 64-bit SoC @ 1.5GHz | 
| Pins | 40 Pin GPIO Header | 
| Voltage | 5V DC via USB-C/GPIO Header |   
| Amperage | 3A |   

### 9.3. Printed Circuit Board (PCB) Specifications

The printed circuit board will be used to combine all the electrical hardware with its respective software interfaces. Using soldering techniques, each wire and resistor will be soldered to its respective hole. The PCB specifications are listed below, referenced from Elegoo [4].

| PCB Specifications | Value |   
|:--|:--|   
| Dimensions | 5cm x 7cm |   
| Thickness | 1.6mm |   
| Material | Glass Giber FR4 |   
| Hole-Pitch | 2.54mm | 
| Hold-diameter | 1mm |   

### 9.4. Resistor Specifications

| Part | Specification |   
|:--|:--|   
| INSERT | SPEC |   
| INSERT | SPEC |   
| INSERT | SPEC |   

## 10. Communication Protocols

### 10.1. USB Protocol
In order to communicate and transmit data, the USB protocol will be used. The following ports will be mainly used for the following: 

| USB | Purpose |   
|:--|:--|   
| USB 3.0 | The USB 3.0 ports will be used to connect to external cameras or other devices like keyboards, mice, external storage devices, and other computers to allow for greater ease-of-use and accessibility. |   
| USB-C | The USB-C port will be used to charge the CRA when the battery falls below the desired power percentage. |    

### 10.2. Wi-Fi Protocol
The Wi-Fi protocol is the 802.11ac protocol. This protocol allows for connections from frequencies of 2.4GHz or 5.0Ghz. This protocol will be used for the following. 

| Wifi Protocol | Purpose |   
|:--|:--|   
| 802.11ac | This wireless protocol will allow the users to connect to the CRA remotely through various methods including SSH. Furthermore, this protocol allows users to connect their CRA to either a 2.4 or 5.0GHz wireless network. | 
## 11. Software Modules

All software modules are classes implemented in Python 3.9. Software modules are constructed and executed by threaded `start.py` classes. The `__main__.py` class should immediately begin running upon startup of the Raspberry Pi OS.

<div align="center">
<p id="css">Figure 11.0.1: CRA Software Stack</p>

![image](https://user-images.githubusercontent.com/46848538/213317988-3e1dbebb-54af-4f58-bcc3-202ff45de1c2.png)

</div>

### 11.1. video_buffer.py

__Module Implementation__

Composed of a class Buffer. Provides the functionality of starting, stopping, and logging a video clip.  

__Module Secrets__

- Video capture instance.
- Frames of video clips.
- Video codec.

__Module Relationships__

Receives the following Buffer class construction parameters through `__init__()`.

| Parameter | Type | Description |
|:--|:--|:--|
| video_length | integer | The length in seconds of the requested video. |
| num_partitions | integer | [2->10] more partitions = higher concatenation time and lower storage usage |
| fps | integer | Number of frames requested from camera every second. |
| save_directory | string | The full directory you wish to save recordings at |
| temp_directory | string | The full directory used to temporarily store .mp4 clips |
| camera_id | integer | -1 -> Automatically detect camera, >=0 -> Manually identify by webcam index |
| resolution | integer | -1 -> Automatically detect resolution, 0 -> 640x480, 1 ->  1280x720, 2 -> 1920x1080 |

__Likely Changes__

- Reduce the number of input parameters to the instantiation of the Buffer class. These inputs will be replaced by fixed parameters which are deemed most suitable.

__Unlikely Changes__

- Change the camera being used from a USB web-camera to the Raspberry Pi Camera Module.
  - Subsequently, a large portion of the code for the Buffer class will have to be rewritten.

### 11.2. acceleration_plot.py

__Module Implementation__

A class named Acceleration_Plot. Provides functions for analyzing and visualizing acceleration data.

__Module Secrets__

- Algorithm for computing if a crash has occurred.
- Implementation details of the live plot.

__Module Relationships__

Receives the following Acceleration_Plot class construction parameters through `__init__()`.

| Parameter | Type | Description |
|:--|:--|:--|
data_points | integer | Maximum number of data points to show on the plot |
average_of | integer | Takes a rolling average of the xyz acceleration points |

Receives incoming acceleration data through `update()`.

| Parameter | Type | Description |
|:--|:--|:--|
| x | float | x component of acceleration |
| y | float | y component of acceleration |
| z | float | z component of acceleration |
| t | float | time |

Computes, using the available acceleration data, and returns if a crash has occurred through `is_crash_detected()`.

| Returns | Description |
|:--|:--|
| boolean | If a crash has been detected |

__Likely Changes__

- Adding the ability to log acceleration data in CSV format, so that data can be collected in the field and brought back to the lab for analysis.
- Crash detection algorithm will likely be updated and refined as manual testing continues.

__Unlikely Changes__

- Functions related to the visualization of acceleration data are useful in testing, but may be removed to improve the performance of the embedded system.

### 11.3. led.py

__Module Implementation__
A class named led. Provides the functionalty of mapping Rasperry Pi pin to LEDs and also turning on/off the individuals LED.


__Module Secrets__

- Rasberry Pi pin setups.
- Implementation of turning the LEDs on/off.

__Module Relationships__

Receives the following led class construction parameters through `__init__()`.

| Parameter | Type | Description |
|:--|:--|:--|
pins | integer | Pin number on the Rasberry Pi for connecting the LEDs |

Turning on the LEDs based on the percentage it is at through `percentage_high()`.

| Parameter | Type | Description |
|:--|:--|:--|
percent | integer | Percentage of LEDs that should be turned on |

__Likely Changes__

- No likely changes

__Unlikely Changes__

- No unlikely changes

### 11.4. ultrasonic_sensor.py

__Module Implementation__
A class named ultrasonic_sensor. Provides the functionalty of measuring the distance of the object using ultrasonic sensor.


__Module Secrets__

- Rasberry Pi pin setups.
- Calculation for the distance of object from ultrasonic sensor.
- Time it takes for the ultrasonic sensor to pikc up the object.

__Module Relationships__

Receives the following led class construction parameters through `__init__()`.

| Parameter | Type | Description |
|:--|:--|:--|
pin_trigger | integer | Pin number on the pi corresponding to the trigger pin on the sensor |

| Parameter | Type | Description |
|:--|:--|:--|
pin_echo | integer | Pin number on the pi corresponding to the echo pin on the sensor |

| Parameter | Type | Description |
|:--|:--|:--|
distance_min | integer | The closest distance that the ultrasonic sensor should detect |

| Parameter | Type | Description |
|:--|:--|:--|
distance_max | integer | The furthest distance that the ultrasonic sensor should detect |

| Parameter | Type | Description |
|:--|:--|:--|
unit | string | Unit of the min and max distances (ex. cm) |


__Likely Changes__

- Number of LEDs.
- Distance unit.
- Maximum and minimum distance the ultrasonic sensor should detect.

__Unlikely Changes__

- No unlikely changes

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
**Camera Resolution:** The maximum camera resolution possible with the current implementation is 640p. This is due to the data transfer speeds being limited by the USB connection made between the camera and the Raspberry Pi. Using the Raspberry Camera Module is an alternative to the current implementation which would overcome the USB bandwidth issue and could increase the resolution to 1080p. This alternative comes with the downside of addition cost and recording software rewriting because the Pi Camera Module uses custom libraries.

**Camera Position:** With the current implementation the camera is seated atop the bicycle forks facing forward. This provides video capture of the volume of space in front of the cyclist. The limitation of this implementation is evident, there is no camera footage of the volume of space behind the rider. An alternative to the current state would be to add an additional camera with a view behind the cyclist. However, due to the current USB bandwidth issues with a single camera and the lack of support for dual Raspberry Pi Camera Modules this change is not feasible. A possible alternative would be changing the position of the current camera to face being the cyclist.

**Battery Life:** For cyclists who go on multi hour long bicycle rides, battery life may be of concern. The Raspberry Pi used to perform computations is not particularly battery efficient compared to more project specific embedded computers who do not have as much computational overhead. The capacity of the current battery pack being used is 10,000mah. To improve battery life, a higher capacity battery pack could be purchased. However, a higher capacity battery pack is almost certain to come along with the unwanted side effects of a larger size and heavier weight. 

 ### 13.2. References

[1] "Raspberry Pi 4 Mechanical Drawing", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-mechanical-drawing.pdf

[2] "What is PLA?", 2023. [Online]. Available: https://www.twi-global.com/technical-knowledge/faqs/what-is-pla

[3] "Raspberry Pi 4 Electrical Schematic", 2018. [Online]. Available: https://datasheets.raspberrypi.com/rpi4/raspberry-pi-4-reduced-schematics.pdf

[4] "Elegoo Double Sided PCB Board Kit", 2023. [Online]. Available: https://www.elegoo.com/en-ca/products/elegoo-double-sided-pcb-board-kit