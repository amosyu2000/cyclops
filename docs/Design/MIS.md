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
- [8. Mechanical Hardware](#8-mechanical-hardware)
- [9. Electrical Components](#9-electrical-components)
- [10. Communication Protocols](#10-communication-protocols)
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

## 7. User Interfaces

## 8. Mechanical Hardware

## 9. Electrical Components

## 10. Communication Protocols

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