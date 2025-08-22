import cv2
import time
import math
import threading
import pyvjoy
import mediapipe as mp


#CONFIG

CAM_INDEX = 0
PROC_WIDTH, PROC_HEIGHT = 128, 128
TARGET_FPS = 120
MAX_HANDS = 2
MODEL_COMPLEXITY = 0
MIN_DET_CONF = 0.5
MIN_TRK_CONF = 0.5
SMOOTH_ALPHA = 0.2  # smoothing for steering
THROTTLE_DEADZONE = 0.2
BRAKE_DEADZONE = 0.2
MIN_DIST_THROTTLE = 0
MAX_DIST_THROTTLE = 80
MIN_DIST_BRAKE = 0
MAX_DIST_BRAKE = 80
DRAW_DEBUG = False



#individual thread for HandDetector to maximize performance
class HandDetector(threading.Thread):
    def __init__(self, cap):
        super().__init__(daemon=True)
        self.cap = cap
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=False,
            max_num_hands=MAX_HANDS,
            min_detection_confidence=MIN_DET_CONF,
            min_tracking_confidence=MIN_TRK_CONF,
            model_complexity=MODEL_COMPLEXITY
        )
        self.lock = threading.Lock()
        self.landmarks = [[], []]
        self.running = True

    def run(self):
        while self.running:
            ret, frame = self.cap.read()
            if not ret:
                continue
            imgRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = self.hands.process(imgRGB)
            with self.lock:
                self.landmarks = [[], []]
                if results.multi_hand_landmarks:
                    for idx, handLms in enumerate(results.multi_hand_landmarks):
                        if idx >= MAX_HANDS:
                            break
                        hand_points = []
                        for id, lm in enumerate(handLms.landmark):
                            h, w, _ = frame.shape
                            hand_points.append([id, int(lm.x * w), int(lm.y * h)])
                        self.landmarks[idx] = hand_points

    def get_landmarks(self):
        with self.lock:
            return [l.copy() for l in self.landmarks]


#Main 
def main():
    cap = cv2.VideoCapture(CAM_INDEX, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, PROC_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, PROC_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, TARGET_FPS)

    if not cap.isOpened():
        raise RuntimeError("Cannot open camera")

    detector = HandDetector(cap)
    detector.start()

    j = pyvjoy.VJoyDevice(1)
    smooth_offset = 0.0

    try:
        while True:
            hands = detector.get_landmarks()
            left_hand, right_hand = hands[0], hands[1]

            if left_hand and right_hand:
                #Steering (X Axis)
                x1, y1 = left_hand[17][1], left_hand[17][2]
                x2, y2 = right_hand[17][1], right_hand[17][2]
                slope = ((y1 - y2) / (x2 - x1)) if (x2 - x1) != 0 else 0.0
                smooth_offset = (1 - SMOOTH_ALPHA) * smooth_offset + SMOOTH_ALPHA * slope
                norm_slope = max(-1.0, min(1.0, smooth_offset))
                x_vjoy = int(0x4000 + norm_slope * 0x4000)
                j.set_axis(pyvjoy.HID_USAGE_X, x_vjoy)

                #Throttle (right thumb)
                x4, y4 = right_hand[4][1], right_hand[4][2]
                x6, y6 = right_hand[6][1], right_hand[6][2]
                dist_throttle = math.hypot(x6 - x4, y6 - y4)
                throttle_val = max(0.0, min(1.0, (dist_throttle - MIN_DIST_THROTTLE) / (MAX_DIST_THROTTLE - MIN_DIST_THROTTLE)))
                if throttle_val < THROTTLE_DEADZONE:
                    throttle_val = 0.0
                else:
                    throttle_val = (throttle_val - THROTTLE_DEADZONE) / (1 - THROTTLE_DEADZONE)
                y_vjoy = int(throttle_val * 0x8000)
                j.set_axis(pyvjoy.HID_USAGE_Y, y_vjoy)

                #Brake (left thumb)
                x8, y8 = left_hand[4][1], left_hand[4][2]
                x10, y10 = left_hand[6][1], left_hand[6][2]
                dist_brake = math.hypot(x10 - x8, y10 - y8)
                brake_val = max(0.0, min(1.0, (dist_brake - MIN_DIST_BRAKE) / (MAX_DIST_BRAKE - MIN_DIST_BRAKE)))
                if brake_val < BRAKE_DEADZONE:
                    brake_val = 0.0
                else:
                    brake_val = (brake_val - BRAKE_DEADZONE) / (1 - BRAKE_DEADZONE)
                z_vjoy = int(brake_val * 0x8000)
                j.set_axis(pyvjoy.HID_USAGE_Z, z_vjoy)

            if DRAW_DEBUG:
                ret, frame = cap.read()
                if ret:
                    cv2.imshow("Debug", frame)
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

    finally:
        detector.running = False
        cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
