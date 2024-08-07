# VisionSteer

<img src="https://github.com/user-attachments/assets/57733174-98c5-4020-a588-f137a8ce0a21" width="400" />


Control your car/vehicle in a game/simulator with a simple steering gesture using your hands or a dinner plate. No need to purchase a physical wheel when you can already imagine yourself in the driver seat!

**Demo video at bottom**

## Installation

To run the script, Python version 3.12 or higher is required. To install Python, visit the official Python downloads page by [Clicking Here](https://www.python.org/downloads/). **Make sure to add Python as a Path/environment variable during installation when prompted** 

To check if the installation is successful, type "python" in command prompt. 

Once Python installation is completed, download the zip file of VisionSteer through Github. Once the download is completed, make sure to extract/unzip the downloaded folder. __Only the unzipped folder is used for the next steps__ 

Running the script requires some necessary packages to be installed into the device. The packages include Mediapipe, OpenCV, and Pynput. A requirements.txt file is included in the repository that allows you to directly install the necessary packages via a command line prompt. 


Open command prompt and traverse to the proper directory where the python script "VisionSteer.py" is located after installing the zip package. For example, after installing from Github, the "VisionSteer.py" file is located in: 


**ALL OF THE FOLLOWING COMMANDS MUST BE RUN WITHIN THE SAME DIRECTORY**:
```bash
C:\Users\prakh\Downloads\VisionSteering-main\VisionSteering-main
```

Once you have entered the correct directory of where "VisionSteer.py" is located, you must install the correct packages using the "requirements.txt" file in the same directory. Simply run the following command in the command line terminal.
```bash
pip install -r requirements.txt
```
After installation is completed, you will be informed that Mediapipe, OpenCV, and Pynput have been installed onto the device directory. 

**Installation is complete**. To begin, simply run the python script "VisionSteer.py" using the command line terminal with the following command:
```bash
python VisionSteer.py
```

After a few seconds, a window will popup showing your camera. 

## Usage
**VisionSteer REQUIRES a Camera**

It is suggested that VisionSteer is primarily used with Assetto Corsa using Content Manager. To download Assetto Corsa, [Click Here](https://store.steampowered.com/app/244210/Assetto_Corsa/)

VisionSteer requires the use of mouse steering in Assetto Corsa (or any other game compatible with such). In Assetto Corsa, it is suggested to use the following settings under Controls of Content Manager for the smoothest experience. Throttle and Brakes must be set to "W" and "S"


![image](https://github.com/user-attachments/assets/a5bc52fe-dbe0-4efd-9a37-bb69285bf16e)

Forced Throttle is not necessary. 

It is also important that the Steering Wheel Limit is set to 180 degrees for the most realistic and smoothest experience. To do so, click the "View and UI" tab in Content Manager under Assetto Corsa and set "Steering wheel limit" to 180 degrees. 

![image](https://github.com/user-attachments/assets/bfe9c68d-e257-434c-b9d3-564e62509d3b)

You are now ready to play. Simply launch your session in Assetto Corsa (or other compatible mouse steering games) and launch the script. 
**To begin, it is suggested that the video game or program you wish to use VisionSteer with is already open.**

### Steps for gesture detection
1) Position your camera where your hands are fully visible and comfortable to place. A demonstration of an ideal camera position is as such: 

   ![image](https://github.com/user-attachments/assets/1c06211a-4011-48c6-8d37-4bb391d38b60)
2) **Steering**: Make a steering wheel gesture with both your fists closed. Center your gestured wheel so that it reflects in the video game. Turn your gestured wheel to the the right or left and the movement will be reflected by the car in the game.  
3) **Accelerating**: To accelerate, lift your right thumb from your closed right fist. When the right thumb is lifted, the car will begin to accelerate. Simply close your thumb with the fist again to stop accelerating. 
4) **Braking**: To brake, lift your left thumb from your closed left fist. When the left thumb is lifted, the car will begin to decelerate. Simply close your thumb with the fist again to stop braking. 


Below is video demo of how Vision Steer works and its proper usage. In this demo, a dinner plate is used for a more realistic experience with added weight, still with the use of your camera. 

https://github.com/user-attachments/assets/87f96ef8-a0af-4d5b-8e81-cbbe4d2682d0

 
