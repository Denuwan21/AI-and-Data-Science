import cv2 as cv
import mediapipe as mp

cap = cv.VideoCapture(0)


hands = mp.solutions.hands
mphands = hands.Hands()
mpdraw = mp.solutions.drawing_utils


while True:
    ret, img = cap.read()
    RGB_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    result = mphands.process(RGB_img)
    #print(result.multi_hand_landmarks)

    if result.multi_hand_landmarks :
        for mplandmars in result.multi_hand_landmarks:
            mpdraw.draw_landmarks(img, mplandmars, hands.HAND_CONNECTIONS)

            for id, lm in enumerate(mplandmars.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                
                if id==0:
                    cv.circle(img, (cx, cy), 10, (200, 100, 225), cv.FILLED)


    cv.imshow('Window', img)
    if cv.waitKey(1) == ord('x'):
        break
  

