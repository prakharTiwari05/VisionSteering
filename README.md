# VisionSteer v2

<img src="https://github.com/user-attachments/assets/57733174-98c5-4020-a588-f137a8ce0a21" width="400" />

**Control your car/vehicle in a game or simulator using simple hand gestures — now with ultra-low latency steering and full vJoy integration!**  
No physical wheel needed; just your hands (or a plate for more realism) and a webcam.

---

## Features

- vJoy integration for **direct steering wheel input** (X, Y, Z axes)  
- Ultra-low latency steering for **accurate and smooth control**  
- Hand gesture recognition using **Mediapipe Hands**  
- Separate thread for hand detection to maximize FPS  
- Gesture-based throttle and brake detection  
- Optional debug camera feed for troubleshooting  

---

## What’s New in Version 2

- **vJoy Integration**: Replaces mouse steering for minimal latency and precise control  
- **Improved Gesture Processing**: Smoothed steering and analog throttle/brake control  
- **Threaded Hand Detection**: Runs on a separate thread for higher performance  
- **Configurable Deadzones**: Avoid accidental inputs for throttle and brake  

---

## Requirements

- Python **3.12 or higher**  
- [vJoy Virtual Joystick](http://vjoystick.sourceforge.net/site/)  
- Python packages from `requirements.txt` (Mediapipe, OpenCV, pyvjoy)  
- Webcam  

---

## Full Setup & Installation

### 1. Install Python

1. Download Python 3.12+ from the official [Python Downloads](https://www.python.org/downloads/) page.  
2. During installation, **check “Add Python to PATH”**.  
3. Verify installation:

```cmd
python --version
```

# VisionSteer v2

VisionSteer v2 allows you to control racing games like Assetto Corsa using hand gestures and vJoy virtual joystick.

---

## 1. Install vJoy

1. Download and install **vJoy** from [vjoystick.sourceforge.net](https://sourceforge.net/projects/vjoystick/).  
2. Open **vJoy Device Configuration** and ensure at least 3 axes are enabled:
   - X-axis (Steering)
   - Y-axis (Throttle)
   - Z-axis (Brake)  
3. Leave axis ranges as default: **0–32768**.  
4. Optional: Calibrate axes in your game for full motion accuracy.  
5. Test using **vJoy Monitor** — axes should respond to hand gestures in real time.

---

## 2. Install VisionSteer v2

1. Download and unzip the **VisionSteer v2** repository from GitHub.  
2. Open Command Prompt and navigate to the folder containing `VisionSteer.py`:

```bash
cd C:\Users\YourUser\Downloads\VisionSteer-v2
```

Install required Python packages:

```cmd
pip install -r requirements.txt
```

## 3. vJoy Axes Mapping
   vJoy Axis	Gesture	Description
   X-axis (HID_USAGE_X)	Steering	Left/right hand rotation gesture
   Y-axis (HID_USAGE_Y)	Throttle	Right thumb lift distance
   Z-axis (HID_USAGE_Z)	Brake	Left thumb lift distance

## 4. In-Game Axis Mapping (Assetto Corsa)

   Open Assetto Corsa → Controls → Steering Wheel.
   
   Map axes as follows:
   
   In-Game Axis	vJoy Axis
   Steering	X-axis
   Throttle	Y-axis
   Brake	Z-axis
   
   Set Steering Wheel Limit → 180° for realistic, smooth control.

## 5. Usage

   Launch your game first (Assetto Corsa recommended).
   
   Run VisionSteer:
   
   ```cmd
   python VisionSteer.py
   ```


   Position your webcam so both hands are fully visible.
   
   Gesture Controls
   Action	Gesture Description
   Steering	Closed-fist wheel gesture with both hands, rotate left/right
   Accelerating	Lift right thumb to accelerate; close to stop
   Braking	Lift left thumb to brake; close to stop

## 6. Optional Debug Mode

   Enable debug mode in VisionSteer.py:
   
   DRAW_DEBUG = True
   
   
   Shows live camera feed with detected hands.
   
   Press q to exit.

## 7. Configuration Parameters

   - **CAM_INDEX**: Index of your camera (0 is default)  
   - **PROC_WIDTH, PROC_HEIGHT**: Frame size for processing  
   - **TARGET_FPS**: Maximum frames per second  
   - **MAX_HANDS**: Maximum number of hands to detect  
   - **MODEL_COMPLEXITY**: Mediapipe hand detection model complexity  
   - **SMOOTH_ALPHA**: Steering smoothing factor  
   - **THROTTLE_DEADZONE / BRAKE_DEADZONE**: Minimum gesture distance to register input  
   - **MIN_DIST_THROTTLE / MAX_DIST_THROTTLE**: Throttle gesture calibration  
   - **MIN_DIST_BRAKE / MAX_DIST_BRAKE**: Brake gesture calibration  
   - **DRAW_DEBUG**: Show camera feed for debug purposes  



