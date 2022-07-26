from gpiozero import Servo
import cv2
import mediapipe as mp

## opencv & mediapipe
cap = cv2.VideoCapture(0)

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

    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)

    for index, servo in enumerate(servo_list):
        servo.value = 1