# Youtube: https://www.youtube.com/watch?v=oIGZ6aYh9LU&ab_channel=AISciences
# GitHub: https://github.com/AISCIENCES/Ytube-finger-counter/blob/main/main.py

# This code is for right hand

import cv2
import mediapipe as mp

cap = cv2.VideoCapture(0)
mpHands = mp.solutions.hands # hands.py module
hands = mpHands.Hands() # object with class "Hands" in hands.py module
mpDraw = mp.solutions.drawing_utils
thumbCoordinate = (4, 3)
fingerCoordinates = [(8, 6), (12, 11), (16, 15), (20, 19)]

while True:
    success, img = cap.read()
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

        count = [0,0,0,0,0]

        # thumb
        if handPoints[thumbCoordinate[0]][0] > handPoints[thumbCoordinate[1]][0]: # less than for left hand
            count[0] += 1

        # other fingers
        for index, coordinates in enumerate(fingerCoordinates):
            if handPoints[coordinates[0]][1] < handPoints[coordinates[1]][1]:
                count[index + 1] += 1

        cv2.putText(img, str(count), (40,100), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Finger Counter", img)
    cv2.waitKey(1)
