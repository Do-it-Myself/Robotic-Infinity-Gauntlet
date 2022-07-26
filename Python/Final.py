# Youtube: https://www.youtube.com/watch?v=oIGZ6aYh9LU&ab_channel=AISciences
# GitHub: https://github.com/AISCIENCES/Ytube-finger-counter/blob/main/main.py
# Library for OpenCV & Mediapipe: https://pypi.org/project/mediapipe-rpi4/
# Library for gpiozero: https://gpiozero.readthedocs.io/en/stable/installing.html

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
count = ["0", "0", "0", "0", "0"]
word = "Nothing"

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

    if multiLandMarks:
        handPoints = []
        for handLms in multiLandMarks:
            # draw hand skeleton
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

            # calculate coordinates of hand points
            for index, lm in enumerate(handLms.landmark):
                height, width, channel = img.shape
                cx, cy = int(lm.x * width), int(lm.y * height)
                handPoints.append((cx, cy))

        # label hand points
        for point in handPoints:
            cv2.circle(img, point, 5, (0, 0, 255), cv2.FILLED)

        # detect left or right hand
        rightHand = False

        if handPoints[fingerCoordinates[0][3]][0] < handPoints[fingerCoordinates[3][3]][0]:
            rightHand = True
        
        # detect whether the hand is placed properly or not
        condi1 = handPoints[thumbCoordinate[3]][1] > handPoints[thumbCoordinate[4]][1]
        condi2 = handPoints[fingerCoordinates[3][3]][1] > handPoints[thumbCoordinate[4]][1]
        condi3_right = handPoints[fingerCoordinates[0][3]][0] > handPoints[thumbCoordinate[4]][0]
        condi3_left = handPoints[fingerCoordinates[0][3]][0] < handPoints[thumbCoordinate[4]][0]


        # reset count
        count = ["0", "0", "0", "0", "0"]

        # check fingers
        if condi1 or condi2 or (rightHand and condi3_right) or (not rightHand and condi3_left):
            word = "Put your hand properly"
        else: 
            # if right hand
            if rightHand:
                word = "Right hand: "
                # thumb
                if handPoints[thumbCoordinate[0]][0] < handPoints[thumbCoordinate[1]][0]:
                    count[0] = "1"
            
            # if left hand
            else: 
                word = "Left hand: "
                # thumb
                if handPoints[thumbCoordinate[0]][0] > handPoints[thumbCoordinate[1]][0]: 
                    count[0] = "1"

            # other fingers
            for index, coordinates in enumerate(fingerCoordinates):
                if handPoints[coordinates[0]][1] < handPoints[coordinates[2]][1]:
                    count[index + 1] = "1"

            word = word +  ' '.join(count)

        cv2.putText(img, str(word), (40,80), cv2.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)

    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)

    ## servo
    for index, servo in enumerate(servo_list):
        if count[index] == "0":
            print(str(index) + ": close")
            servo.value = -1
        elif count[index] == "1":
            print(str(index) + ": open")
            servo.value = 1
    print("")
