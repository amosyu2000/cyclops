<div align="center">

<a href="https://github.com/amosyu2000/cyclops">
    <img src="../../refs/header.svg" width="800" height="400" alt="Cyclops header">
</a>

# System Verification and Validation Plan <!-- omit in toc -->
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
- [2. Symbols, Abbreviations, and Acronyms](#2-symbols-abbreviations-and-acronyms)
- [3. General Information](#3-general-information)
	- [3.1. Purpose](#31-purpose)
	- [3.2. Scope](#32-scope)
	- [3.3. Relevant Documentation](#33-relevant-documentation)
- [4. Plan](#4-plan)
	- [4.1. Verification and Validation Team](#41-verification-and-validation-team)
	- [4.2. SRS Verification Plan](#42-srs-verification-plan)
	- [4.3. Design Verification Plan](#43-design-verification-plan)
	- [4.4. Verification and Validation Plan Verification Plan](#44-verification-and-validation-plan-verification-plan)
	- [4.5. Implementation Verification Plan](#45-implementation-verification-plan)
	- [4.6. Automated Testing and Verification Tools](#46-automated-testing-and-verification-tools)
	- [4.7. Software Validation Plan](#47-software-validation-plan)
- [5. System Test Description](#5-system-test-description)
	- [5.1. Tests for Functional Requirements](#51-tests-for-functional-requirements)
		- [5.1.1. Vehicle Detection Test](#511-vehicle-detection-test)
		- [5.1.2. Accelerometer Value Test](#512-accelerometer-value-test)
		- [5.1.3. Crash Detection Test](#513-crash-detection-test)
		- [5.1.4. Video Logging Test](#514-video-logging-test)
		- [5.1.5. Full SD Test](#515-full-sd-test)
		- [5.1.6. Resume Detection Test](#516-resume-detection-test)
		- [5.1.7. Front Light On Test](#517-front-light-on-test)
		- [5.1.8. Front Light Off Test](#518-front-light-off-test)
		- [5.1.9. Power On System Test](#519-power-on-system-test)
		- [5.1.10. Power Off System Test](#5110-power-off-system-test)
	- [5.2. Tests for Nonfunctional Requirements](#52-tests-for-nonfunctional-requirements)
		- [5.2.1. Appearance and Style Tests](#521-appearance-and-style-tests)
		- [5.2.2. Ease of Use Tests](#522-ease-of-use-tests)
		- [5.2.3. John Doe](#523-john-doe)
		- [5.2.4. Learning Tests](#524-learning-tests)
		- [5.2.5. Understandability Tests](#525-understandability-tests)
		- [5.2.6. Accessibility Tests](#526-accessibility-tests)
		- [5.2.7. Speed and Latency Tests](#527-speed-and-latency-tests)
		- [5.2.8. John Doe](#528-john-doe)
		- [5.2.9. John Doe](#529-john-doe)
		- [5.2.10. John Doe](#5210-john-doe)
		- [5.2.11. John Doe](#5211-john-doe)
		- [5.2.12. John Doe](#5212-john-doe)
		- [5.2.13. Safety-Critical Tests](#5213-safety-critical-tests)
		- [5.2.14. John Doe](#5214-john-doe)
		- [5.2.15. John Doe](#5215-john-doe)
		- [5.2.16. Precision and Accuracy Tests](#5216-precision-and-accuracy-tests)
		- [5.2.17. John Doe](#5217-john-doe)
		- [5.2.18. John Doe](#5218-john-doe)
		- [5.2.19. Reliability and Availability Test](#5219-reliability-and-availability-test)
		- [5.2.20. Robustness and Fault-Tolerance Tests](#5220-robustness-and-fault-tolerance-tests)
		- [5.2.21. Capacity Tests](#5221-capacity-tests)
		- [5.2.22. Scalability and Extensibility Tests](#5222-scalability-and-extensibility-tests)
		- [5.2.23. Longevity Tests](#5223-longevity-tests)
		- [5.2.24. Physical Environment Tests](#5224-physical-environment-tests)
		- [5.2.25. Interfacing with Adjacent Systems Test](#5225-interfacing-with-adjacent-systems-test)
		- [5.2.26. Productization and Release Tests](#5226-productization-and-release-tests)
		- [5.2.27. Maintenance Tests](#5227-maintenance-tests)
		- [5.2.28. Adaptability Tests](#5228-adaptability-tests)
		- [5.2.29. Access Tests](#5229-access-tests)
		- [5.2.30. Privacy Tests](#5230-privacy-tests)
		- [5.2.31. Cultural Tests](#5231-cultural-tests)
		- [5.2.32. Compliance Tests](#5232-compliance-tests)
		- [5.2.33. Standards Tests](#5233-standards-tests)
- [6. Unit Tests](#6-unit-tests)
	- [6.1. Unit Testing Scope](#61-unit-testing-scope)
	- [6.2. Test for Functional Requirements](#62-test-for-functional-requirements)
		- [6.2.1. Module X](#621-module-x)
		- [6.2.2. Module X](#622-module-x)
	- [6.3. Test for Nonfunctional Requirements](#63-test-for-nonfunctional-requirements)
		- [6.3.1. Module X](#631-module-x)
		- [6.3.2. Module X](#632-module-x)
- [7. Appendix](#7-appendix)
	- [7.1. Symbolic Parameters](#71-symbolic-parameters)
	- [7.2. Usability Survey Questions?](#72-usability-survey-questions)
- [8. Reflection](#8-reflection)
## List of Tables <!-- omit in toc -->
- [Table 1.1: Revision History](#rh)

## List of Figures <!-- omit in toc -->

## 1. Revision History
<div align="center">

<p id="rh">Table 1.1: Revision History</p>

| Date | Developer(s) | Change |
|:--|:--|:--|
| October 25, 2022 | Aaron Li, Amos Cheung, Amos Yu, Brian Le, Manny Lemos | Document created |

</div>

## 2. Symbols, Abbreviations, and Acronyms
| Name | Description |
|:--|:--|
| CRA | Abbreviation of Cyclops Ride Assist.|
| Cyclist | A person who operates a bicycle as a means of transportation. |
| User | A person who will operate the final product. See Cyclist. |
| Client | See user. |
| SRS | Software Requirements Specification |




## 3. General Information
### 3.1. Purpose
The purpose of this document is to describe the testing, validation, and verification processes which will be carried out on the CRA system. Testing instills confidence that software and hardware function as expected independently, and interface correctly. 
### 3.2. Scope
This validation and verification document lays the foundation for testing the CRA system. The requirements for correct system functionality presented in the SRS document will be extended upon to include specific, quantifiable metrics. Success in the testing described will verify that CRA has met these requirements in a measurable, meaningful way.

Specifically, this document will address testing pertaining to both the software and hardware of CRA. Out of scope testing would include testing for requirements not covered in the SRS document. 
### 3.3. Relevant Documentation
[SRS Document](https://github.com/amosyu2000/cyclops/blob/main/docs/SRS/SRS.md)
## 4. Plan
### 4.1. Verification and Validation Team
There will be two distinct subgroups of the verification and validation team.

Group one will be responsible for any hardware testing. This includes testing of the CRA housing, mount, circuitry, sensors, and video feeds. This group will be composed of Amos Cheung, Aaron Li, and Manny Lemos.

Group two will be responsible for software testing. This includes testing of the CRA crash detection, video logging, and vehicle blindspot detection. This group will be composed of Brian Le and Amos Yu.
### 4.2. SRS Verification Plan
The SRS document has been verified as correct and complete using a number of methods. The Cyclops team has discussed the continued validity of this document and its requirements in team meetings. Further, peer reviews have been conducted on the document, concerns were raised, and issues were resolved.
### 4.3. Design Verification Plan
Our design verification plan to fufill modular testing requirements is composed of two distinct sections; software unit testing, and modular hardware testing.

Software unit testing will be performed using pytest. As new modules of code are developed, or existing modules are updated and features are changed, thorough black box and white box testing will be conducted to verify correct functionality.

Modular hardware testing will occur as discrete components of the hardware are completed. This means that components such as the bicycle mount, will be tested independently of the housing to verify that the component functions as expected. This will act as a baseline for assumed hardware functionality, and will enable the CRA team to identify sources of hardware failure more efficiently.
### 4.4. Verification and Validation Plan Verification Plan
This document will be extensively reviewed by group members as project development progresses. The continued validity of this document will be maintained, and any missing information will be rectified. Moreover, peer reviews will be conducted. If any issues are presented, they will be addressed and resolved. 
### 4.5. Implementation Verification Plan
Will involve static and dynamic techniques
Plan for fulfilling systemwide implementation tests
### 4.6. Automated Testing and Verification Tools
All automated testing of software will be conducted using Pytest. 
### 4.7. Software Validation Plan
To validate that the software fufills all of the right requirements, we will continually amend and improve upon the testing methodologies used, and the components tested. The aim of this endeaver is to ensure that testing is directly aligned with any updates the the SRS document and any other documents which are directly tied to software requirements.
## 5. System Test Description
### 5.1. Tests for Functional Requirements
#### 5.1.1. Vehicle Detection Test
| CFRST1                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.2. Accelerometer Value Test
| CFRST2                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.3. Crash Detection Test
| CFRST3                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.4. Video Logging Test
| CFRST4                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.5. Full SD Test
| CFRST5                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.6. Resume Detection Test
| CFRST6                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.7. Front Light On Test
| CFRST7                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.8. Front Light Off Test
| CFRST8                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.9. Power On System Test
| CFRST9                        | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.1.10. Power Off System Test
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
### 5.2. Tests for Nonfunctional Requirements
#### 5.2.1. Appearance and Style Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.2. Ease of Use Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.3. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.4. Learning Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.5. Understandability Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.6. Accessibility Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.7. Speed and Latency Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.8. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.9. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.10. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.11. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.12. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.13. Safety-Critical Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.14. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.15. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.16. Precision and Accuracy Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.17. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.18. John Doe
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.19. Reliability and Availability Test
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.20. Robustness and Fault-Tolerance Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.21. Capacity Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.22. Scalability and Extensibility Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.23. Longevity Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.24. Physical Environment Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.25. Interfacing with Adjacent Systems Test
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.26. Productization and Release Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.27. Maintenance Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.28. Adaptability Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.29. Access Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.30. Privacy Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.31. Cultural Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.32. Compliance Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 5.2.33. Standards Tests
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
## 6. Unit Tests
### 6.1. Unit Testing Scope
### 6.2. Test for Functional Requirements
#### 6.2.1. Module X
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 6.2.2. Module X
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
### 6.3. Test for Nonfunctional Requirements
#### 6.3.1. Module X
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
#### 6.3.2. Module X
| CFRST10                       | |
|:--                            |:--|
| Control                       | sus |
| Initial State                 | sus |
| Input                         | sus |
| Output                        | sus |
| Test Case Derivation          | sus |
| How will test be performed    | sus |
| Requirements Referenced       | sus |
## 7. Appendix
### 7.1. Symbolic Parameters
### 7.2. Usability Survey Questions?
Could CRA be set up and installed by a non-technical user?
Would the size of the device be an encumbrance to a typical cyclist.
## 8. Reflection
What knowledge and skills do we need to acquire for VnV?
Where can we acquire these skills? -> Which option do we choose
Talk about automated testing tools that we had to learn about mes


