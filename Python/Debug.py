from gpiozero import Servo
import cv2
import mediapipe as mp

## opencv & mediapipe
cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands # hands.py module
hands = mpHands.Hands() # object with class "Hands" in hands.py module
mpDraw = mp.solutions.drawing_utils
thumbCoordinate = (4, 3, 2, 1, 0)
fingerCoordinates = [(8, 7, 6, 5), (12, 11, 10, 9), (16, 15, 14, 13), (20, 19, 18, 17)]

## servo
servo1 = Servo(23, min_pulse_width = 0.33/1000)
servo2 = Servo(24, min_pulse_width = 0.33/1000)
servo3 = Servo(25, min_pulse_width = 0.33/1000)
servo4 = Servo(8, min_pulse_width = 0.33/1000)
servo5 = Servo(7, min_pulse_width = 0.33/1000)
servo_list = [servo1, servo2, servo3, servo4, servo5]

while True:
    success, img = cap.read()
    img = cv2.flip(img, 0)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # process hand image with mediapipe
    results = hands.process(imgRGB)
    multiLandMarks = results.multi_hand_landmarks

    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)

    for index, servo in enumerate(servo_list):
        servo.value = 1