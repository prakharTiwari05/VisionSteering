import cv2
import time
import HandTrackingModule as htm
import math
import pynput.mouse as ms
import pynput.keyboard as kb
import ctypes

user32 = ctypes.windll.user32


mouse = ms.Controller()
keyboard = kb.Controller()

screenWidth = user32.GetSystemMetrics(0)
screenHeight = user32.GetSystemMetrics(1)
widthCam, heightCam = 300, 300
centerX = screenWidth//2
yCenter = screenHeight//2
mouse.position = (centerX, yCenter)
cap = cv2.VideoCapture(0)
cap.set(4, heightCam)
cap.set(3, widthCam)
cap.set(cv2.CAP_PROP_FPS, 60)
pTime = 0
detector = htm.handDetector(detectionCon=0.5)

mouseSens = 50

while True:
    success, img = cap.read()
    if not success:
        continue

    img = detector.findHands(img)
    landmarks1 = detector.findPosition1(img, draw=False)
    landmarks2 = detector.findPosition2(img, draw=False)

    if len(landmarks1) != 0 and len(landmarks2) != 0:
        #for calculating steering angle
        x1, y1 = landmarks1[17][1], landmarks1[17][2]
        x2, y2 = landmarks2[17][1], landmarks2[17][2]
        slope = (y1 - y2) / (x2 - x1) if x2 != x1 else 0
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)

        # show diagram of circle/wheel for display purposes
        wheelX = (x1 + x2)//2
        wheelY = (y1 + y2)//2
        radius = 50
        cv2.circle(img, (wheelX, wheelY), radius, (255, 0, 0), 2)

        #for calculating throttle
        x4, y4 = landmarks2[4][1], landmarks2[4][2]
        x6, y6 = landmarks2[6][1], landmarks2[6][2]
        distanceThrottle = math.sqrt((x6 - x4) ** 2 + (y6 - y4) ** 2)

        #for calculating brake
        x8, y8 = landmarks1[4][1], landmarks1[4][2]
        x10, y10 = landmarks1[6][1], landmarks1[6][2]
        distanceBrake = math.sqrt((x10 - x8) ** 2 + (y10 - y8) ** 2)



        #calculate how much to move the mouse in regards to the steering angle
        move_x = int(slope * mouseSens)


        updatedX = centerX + move_x
        updatedX = max(0, min(screenWidth, updatedX))
        mouse.position = (updatedX, yCenter)

        #detect whether to accelerate or decelerate.
        if distanceThrottle > 40:
            keyboard.press("w")
        else:
            keyboard.release("w")

        if distanceBrake > 40:
            keyboard.press("s")
        else:
            keyboard.release("s")

        # print("DistanceThrottle: ", distanceThrottle)
        # print("DistanceBrake: ", distanceBrake)



    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

    # Display image
    cv2.imshow("Img", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

