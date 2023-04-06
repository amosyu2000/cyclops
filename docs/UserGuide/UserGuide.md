<div align="center">

<a href="https://github.com/amosyu2000/cyclops">
	<img src="../../refs/header.svg" width="800" height="400" alt="Cyclops header">
</a>

# User Guide <!-- omit in toc -->
Cyclops Ride Assist: Cyclops Ride Assist: Real-Time Monitoring System<br/>  
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
- [2. Legal and Copyright Information and Disclaimer](#2-legal-and-copyright-information-and-disclaimer)
- [3. Introduction](#3-introduction)
- [4. Hardware Installation](#4-hardware-installation)
  - [4.1. Hardware Overview](#41-hardware-overview)
  - [4.2. Main Housing Assembly](#42-main-housing-assembly)
  - [4.3. Rear Housing Assembly](#43-rear-housing-assembly)
  - [4.4. Mounting and Dismounting the CRA](#44-mounting-and-dismounting-the-cra)
    - [4.4.1. Mounting the Main Housing of the CRA](#441-mounting-the-main-housing-of-the-cra)
    - [4.4.2. Mounting the Rear Housing of the CRA](#442-mounting-the-rear-housing-of-the-cra)
- [5. Instructions on Using the CRA](#5-instructions-on-using-the-cra)
  - [5.1. Pre-Trip Power On Sequence](#51-pre-trip-power-on-sequence)
  - [5.2. Post-Trip Power Off Sequence](#52-post-trip-power-off-sequence)
  - [5.3. Logging Data from the CRA](#53-logging-data-from-the-cra)
  - [5.4. Interpreting a Capture Sequence Debug](#54-interpreting-a-capture-sequence-debug)
  - [5.5. Retrieving the Video, LiDAR, and Accelerometer Data](#55-retrieving-the-video-lidar-and-accelerometer-data)
- [6. Troubleshooting](#6-troubleshooting)
- [7. Frequently Asked Questions](#7-frequently-asked-questions)

## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)
- [Table 4.1: All Hardware Components](#hc)

## List of Figures <!-- omit in toc -->
- [Figure 3.1: The Cyclops Ride Assist](#cra)  
- [Figure 4.1: Hardware Components of the Cyclops Ride Assist](#hcra)  
- [Figure 4.2: The Main Housing of the Cyclops Ride Assist (CAD)](#mh)
- [Figure 4.3: The Internals of the Main Housing of the Cyclops Ride Assist](#mhi)
- [Figure 4.4: The Rear Housing of the Cyclops Ride Assist (CAD)](#rhc)
- [Figure 4.5: The Main Housing of the Cyclops Ride Assist](#mhca)
- [Figure 4.6: The Rear Housing of the Cyclops Ride Assist](#rhca)
- [Figure 4.7: The Clamp of the Cyclops Ride Assist](#crac)
- [Figure 5.1: The Cyclops Ride Assist on a Bicycle](#bike)
- [Figure 5.2: The On and Off Button of the Cyclops Ride Assist](#onof)
- [Figure 5.3: The Capture Button of the Cyclops Ride Assist](#capt)
- [Figure 5.4: The Special LEDs of the Cyclops Ride Assist](#ledc)
- [Figure 5.5: The Sliding Door and USB Access of the Cyclops Ride Assist](#sdus)

## 1. Revision History
<div align="center">
<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| April 5, 2023 | Aaron Li, Manny Lemos | Document created |

</div>

## 2. Legal and Copyright Information and Disclaimer

The Cyclops Ride Assist as well as its accompanying documentation is licensed under the Cyclops Team in the Department of Computing and Software (CAS) at McMaster University. All Hardware and Software is the intellectual property of CAS. CAS reserves the right to nullify any aspect or agreement in the Cyclops Ride Assist as well as in its accompanying documentation with no prior notice.

As the product has been deemed open-source, you may develop or re-create the Product for personal, non-commercial, or commercial use as you deem fit with the proper citations. The Team and CAS will not be held liable in the event of any possible hazards or consequences created from the Product that may or may not be limited to physical, mental, health damages, technical issues, or factors out of the Team's control.

By using this product, you accept and agree to be bound by the Terms and Conditions. 

Copyright © 2023 Cyclops, Department of Computing and Software (CAS), McMaster University. 

## 3. Introduction

This document is the User Guide for the Cyclops Ride Assist (CRA). It will cover all required installations, assemblies, mounting and dismounting, and proper usage. Furthermore, some common troubleshooting techniques will be introduced as well as some frequently asked questions. 
The CRA is an all-in-one, easily mountable, and quick to setup system that adds modern car safety features onto a bicycle or motorcyCle. These features include rear vehicle detection, crash detection, and automatic video and data capture with upload. This ensures that the Cyclops Ride Assist can be immediately used out of package. The User Guide will thus outline the best practices on mounting the CRA to their own personal bicycle.

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230203454-a10e37b5-94bb-4044-a443-87853cd6be5f.png)  

<p id="cra">Figure 3.1: The Cyclops Ride Assist</p>
</div>

## 4. Hardware Installation 
### 4.1. Hardware Overview

As the Cyclops Ride Assist is a complete product consisting of both hardware and software, it is imperative to correctly install both to ensure proper use. This section will outline the proper technique required to do so. Both the main and rear housing assembly will be pre-assembled prior to delivery to a user.

Pictured below in Figure 3.1 are the components of the Cyclops Ride Assist. Cables are provided. Batteries are not included.

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230207776-b37baa57-a63f-4db7-b4d9-804fbff63698.png)

<p id="hcra">Figure 4.1: All hardware components of the Cyclops Ride Assist.</p>
</div>

<div align="center">

| Hardware Component Name | Assembly Location| Number of Pieces |
|:--|:--|:--|
| Raspberry Pi Model B | Main Housing | 1 |
| 1080p USB Camera  | Main Housing | 1 |
| Accelerometer ADXL-345 | Main Housing | 1 |
| Adafruit Neopixel LED Striplight | Main Housing | 1 |
| On, Off, Capture Push Button | Main Housing | 3 |
| Main Housing (Top) | Main Housing | 1 |
| Main Housing (Middle) | Main Housing | 1 |
| Main Housing (Bottom) | Main Housing | 1 |
| Clamp for Main Housing (Top) | Main Housing | 1 |
| Clamp for Main Housing (Bottom) | Main Housing | 2 |
| Sliding Door | Main Housing | 1 |
| Camera Slot | Main Housing | 1 |
| LED Housing Slot | Main Housing | 1 |
| TF-Luna LiDAR Sensor  | Rear Housing | 1 |
| Rear Housing | Main Housing | 1 |
| Clamp for Rear Housing (Top) | Rear Housing | 1 |
| M2 x 20mm Nuts | Main and Rear Housing | 22 |
| M2 Bolts | Main and Rear Housing | 22 |
<p id="hc">Table 4.1: All Hardware Components of the Cyclops Ride Assist</p>
</div>

### 4.2. Main Housing Assembly
The Main Housing Assembly will come pre-assembled to the users. All external components can be purchased through approved third party vendors and the 3D printed components will be sourced locally. 

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230234430-261e3437-b42e-4a2e-8186-926df41806a3.png)

<p id="mh">Figure 4.2: The Main Housing of the Cyclops Ride Assist.</p>
</div>

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230203395-acfea1a8-37d9-41f6-89f6-f04d125214a8.png)

<p id="mhi">Figure 4.3: The Internals of the Main Housing of the Cyclops Ride Assist.</p>
</div>

### 4.3. Rear Housing Assembly
The Rear Housing Assembly will come pre-assembled to the users. All external components can be purchased through approved third party vendors and the 3D printed components will be sourced locally. 

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230205149-dfe55daa-fac2-4bc4-9f0e-11d0c3eb50f9.png)

<p id="rhc">Figure 4.4: The Rear Housing of the Cyclops Ride Assist (CAD).</p>
</div>

### 4.4. Mounting and Dismounting the CRA

#### 4.4.1. Mounting the Main Housing of the CRA
| Step Number |  Instruction |
|:--|:--|
| 1 | Securely mount the CRA to your bicycle. |
| 2 | Place the housing clamp onto the handlebars of your bicycle. Tighten the clamp by spinning the tightener clockwise. | 
| 3 | Ensure the camera is facing forward. |
| 4 | Ensure the LED strip is visible while seated in your riding position. |
| 5 | Ensure all cables are securely strapped to the bicycle such that no cable is overhanging.|
<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230205047-d7df0870-72f6-4ef6-9720-a9e789e822cc.png)
<p id="mhca">Figure 4.5: The Main Housing of the Cyclops Ride Assist.</p>
</div>   

#### 4.4.2. Mounting the Rear Housing of the CRA

| Step Number |  Instruction |
|:--|:--|
| 1 | Complete [Section 4.4.1.](#441-mounting-the-main-housing-of-the-cra)|
| 2 | Place the rear clamp onto the seat bar of your bicycle. Tighten the clamp by spinning the tightener clockwise. | 
| 2 | Ensure the LiDAR sensor is facing away from the bicycle and is level. |
| 3 | Ensure all cables are securely strapped to the bicycle such that no cable is overhanging.|

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230204971-77066d39-cb66-4949-95ab-6a6041329438.png)


<p id="rhca">Figure 4.6: The Main Housing of the Cyclops Ride Assist (CAD).</p>
</div>

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230236373-b0dd5373-9828-4781-a054-8fae48d8fac0.jpg)


<p id="crac">Figure 4.7: The Clamp of the Cyclops Ride Assist (CAD).</p>
</div>

## 5. Instructions on Using the CRA
Below are the instruction on how to use the CRA once fully assembled on a bicycle. Please ensure that the previous sections have already been completed.

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230235391-2f691f03-f6ab-4b29-9488-3c5690de6e7d.png)


<p id="bike">Figure 5.1: The Cyclops Ride Assist Mounted Properly on a Bicycle.</p>
</div>

### 5.1. Pre-Trip Power On Sequence
In order to setup the CRA prior to a trip, please do the following: 

| Step Number |  Instruction |
|:--|:--|
| 1 | Securely mount the CRA to your bicycle using [Section 4.4](#44-mounting-and-dismounting-the-cra) above. |
| 2 | Locate a portable battery capable of consistently outputting 5V. |
| 2a | Ensure the battery is charged beyond 60%. |
| 3 | Securely fasten the battery into the battery carrying pouch. |
| 4 | Connect the USB power cable to the battery. |
| 5 | Power on the battery. |
| 6 | Press the WHITE button labeled '1' located on the left side of the main housing. |
| 7 | Wait for the GREEN welcome sequence on the LEDs. |
| 8 | Begin your trip. |

### 5.2. Post-Trip Power Off Sequence
In order to turn off the CRA after a trip, please do the following: 

| Step Number |  Instruction |
|:--|:--|
| 1 | Press the black Power Off button labeled ‘0’ located on the left side of the main housing and as seen in Figure 5.2 below. |
| 2 | Wait for the RED goodbye sequence on the LEDs. |
| 3 | Power off your portable battery. |
| 4 | Remove the CRA from your bicycle. |

<br/>
<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230238118-fcde1b67-4162-4a03-b6c3-c48cf24c1878.png)


<p id="onof">Figure 5.2: The On and Off Button.</p>
</div>

### 5.3. Logging Data from the CRA
In the event of a system recognized collision, data logging will occur automatically 10 seconds after the crash without any user intervention. 

Logging can also occur when the user presses the BLUE capture button on the side of the main housing.  

| Step Number |  Instruction |
|:--|:--|
| 1 | Ensure the Pre-Trip Power On Sequence has been followed completely. |
| 2 | Press the BLUE capture button labelled with a camera icon located on the right side of the main housing. |

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230238310-926390da-5976-4b80-ac5c-e549ea242ffb.png)


<p id="capt">Figure 5.3: The Capture Button.</p>
</div>

### 5.4. Interpreting a Capture Sequence Debug

Following a system detected collision or capture button press, the CRA will do the following actions automatically: 

| Action |  Instruction |
|:--|:--|
| 1 | Following a system detected crash or capture button press, the CRA will log 60 seconds of accelerometer, camera, and LiDAR data.  |
| 2 | Following the logging, the user is notified separately of the success or failure of each of these 3 logging events. |
| 3 | Wait between 0 to 10 seconds after a system detected crash or capture button press for all footage and data to log.|
| 4 |Note the blinking color of the 3 LEDs closest to the user. Blue would indicate a SUCCESS and red would indicate a FAILURE. Please refer to [Section 6: Troubleshooting](#6-troubleshooting) for further help.|
| 4a |The LEDs correspond to: <br/> Accelerometer (closest LED to user)<br/>  Camera (2nd closest LED to user) <br/> LiDAR (3rd closest LED to user)|

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230238556-ce3f04fc-68f9-4a33-bd2d-e09a18e0130a.png)


<p id="ledc">Figure 5.4: The Special LED Buttons.</p>
</div>

### 5.5. Retrieving the Video, LiDAR, and Accelerometer Data
In order to view the video footage, LiDAR files, or accelerometer data files, a personal computer must be used. The following steps will outline how to do so.

| Step |  Instruction |
|:--|:--|
| 1 | Open the sliding door on the rear of the main housing to expose the USB stick.  |
| 2 | Pull the USB stick out of the USB port.  |
| 3 | Plug the USB stick into your device (personal computer, laptop, etc.)|
| 4 |Copy any videos or files you would like to save onto your device. All files are located inside "Capture" folders.|
| 5 |(OPTIONAL) Reformat the USB stick as FAT32 to wipe all data.|

<div align="center">

![image](https://user-images.githubusercontent.com/58313755/230239732-01efd96a-f338-4be5-902c-b6ef7d6d9a83.png)


<p id="sdus">Figure 5.5: The Sliding Door for USB Access.</p>
</div>

## 6. Troubleshooting
In the event of an error, please do the following: 

| Action |  Instruction |
|:--|:--|
| 1 | Determine the cause of the issue (accelerometer, camear, LiDAR) based on the LED lights as outlined in Step 3 and 4 of [Section 5.4](#54-interpreting-a-capture-sequence-debug) |
| 1a | If the accelerometer is the issue, open the CRA Main Housing. Check to see if the accelerometer cables are properly connected to the microcontroller. |
| 1b | If the camera is the issue, open the CRA Main Housing. Check to see if the camera cables are properly connected to the microcontroller.|
| 1c | If the LiDAR is the issue, ensure that the wires are connected properly at the CRA Rear Housing.|
| 2 | If the above actions do not work, please power off the CRA using the BLACK button under the '0', wait 30s, and then power it on using the WHITE button under the '1' button.|
| 3 | If the above actions do not work, please power off the CRA through the battery, wait 30s, re-power on the battery, and then power the CRA on using the WHITE button under the '1' button.|

## 7. Frequently Asked Questions 
Q: Will the CRA system work with my bicycle?   
A: CRA is intended to work with all modern bicycles. Its universal clamp can grip posts from 1” up to 3.5” in diameter.

Q: Where can I ask further questions about the Cyclops Ride Assist? Where can I submit a ticket for an issue?
A: An issue or question can be created on our repository, available [here](https://github.com/amosyu2000/cyclops) on Github.
 

Q: How can I contribute to the Cyclops Ride Assist software/hardware?   
A: All of our software and hardware drawings are open-source and available  [here](https://github.com/amosyu2000/cyclops) on Github.
