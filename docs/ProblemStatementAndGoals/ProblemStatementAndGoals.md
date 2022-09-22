<div style="text-align: center;"> 
    <H2 id="Document_Title"> 
        4TB6A: Problem Statement and Goals 
        <br>
        Cyclops 
    </H2>
    <p id="Author_Info">Manny Lemos - lemosm1</p>
    <br><br>
    <p id="Revision_History">
        Table 1: Revision History
        <table style="width: 100%; text-align: left;">
            <tr>
                <th>Date</th>
                <th>Developer(s)</th>
                <th>Change</th>
            </tr>
            <tr>
                <td>2022-09-19</th>
                <td>Manny Lemos, Aaron Li, Amos Yu</th>
                <td>Document Created</th>
            </tr>
        </table>
    </p>
    <br><br>
</div>

## 1. Problem Statement
Cycling is an economic mode of transportation which has a negligible impact on the environment. As North America pursues greener goals, is expected that more people will adopt cycling as their primary method of commuting. However, many North American roads were not designed with cyclists in mind; some roads do not have any bike lanes to speak of, and many of those that do are nothing more than additional paint on an already narrow lane-way. Naturally, a combined road where multi-ton vehicles are speeding past cyclists is a breeding ground for grave bodily injury to cyclists, and leaves the opportunity for motorists to commit hit-and-run crimes.

## 2. Goals

### 2.1. Reliable Blindspot Monitoring
As long as it is mounted to the bicycle, the system will detect if there are objects in the cyclist's blindspots. The system will notify the cyclist that there is an object in their blindspot without requiring them to take their eyes off of the road.

### 2.2. Convenient Mounting and Dismounting
The cyclist will be able to mount the system to the bicycle and unmount the system from the bicycle with minimal effort. When mounted, the system will be secure and will not unmount except if unmounted by the cyclist or under extreme circumstances.

### 2.3. Accurate Crash Detection
As long as it is mounted on the bicycle, the system will collect data on the movement of the bicycle. The system will interpret if the cyclist has been involved in one of many types of accidents (crashing into something, getting hit by something, falling off) with a high degree of accuracy. 

### 2.4. Video Buffering and Saving
As long as it is mounted on the bicycle, the system will collect video footage. The system will buffer the past BUFFER_TIME_MINUTES minutes of footage and will delete all older footage. In the event of an accident, the system will save the buffer footage. The user will be able to access saved footage.

### 2.5. Headlamp
The user will be able to turn on and off the headlamp.When turned on, the headlamp will illuminate the path in front of the bicycle in low-light conditions. When turned on, the headlamp will not decrease the quality of the video footage.

## 3. Stretch Goals

### 3.1. Emergency Response Integration
Call saved Emergency Contact for the user in the case of any accidents. 

### 3.2. Mobile App
The user will be able to interface with the system via the mobile app. The user will be able to use the app to set certain parameters for the system. The system will be able to transfer save footage to the user's smartphone via the mobile app.

### 3.3. Map Integration
Record the distance and places/roads travelled from start to finish on the mobile app. GPS Detection to alert the User of any road closures, accidents, heavy traffic. 

## 4. Appendix

### 4.1. Symbolic Parameters
BUFFER_TIME_MINUTES - The length of footage that will be saved after an accident occurs (in minutes). 