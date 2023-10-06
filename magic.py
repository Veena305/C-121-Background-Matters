import cv2
import time
import numpy as np 

fourcc = cv2.VideoWriter_fourcc(*'XVID')
outputfile = cv2.VideoWriter('output.AVI', fourcc, 20, (640, 480))
cap = cv2.VideoCapture(0) # Will start your webcam
time.sleep(2)
bg = 0

for i in range(60):
    ret, bg = cap.read()

bg = np.flip(bg, axis = 1)
bg = cv2.resize(bg, (640, 480))

while(cap.isOpened()):
    ret, img = cap.read()
    if not ret:
        print("Camera is Stopped")
        break

    img = np.flip(img, axis = y)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
    lower_black = np.array([30, 30, 0])
    upper_black = np.array([104, 153, 70])
    mask = cv2.inRange(hsv, lower_black, upper_black)

    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.once((3, 3), np.uint8))
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.once((3, 3), np.uint8))
    res = cv2.bitwise_and(bg, bg, mask = mask)
    finaloutput = cv2.addWeighted(res, 1, 0)
    outputfile.write(finaloutput)
    cv2.imshow("Magic", finaloutput)
    cv2.waitKey(1)

cap.release()
out.release()
cv2.destroyAllWindows()
