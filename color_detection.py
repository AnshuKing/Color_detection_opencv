import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)


    lower_green = np.array([40,70,80])
    upper_green = np.array([70,255,255])

    lower_red = np.array([0,50,120])
    upper_red = np.array([10,255,255])

   
    mask_green = cv2.inRange(hsv_frame, lower_green, upper_green)
    mask_red = cv2.inRange(hsv_frame, lower_red, upper_red)
    
   
    (cnts_green,_) = cv2.findContours(mask_green, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    (cnts_red,_) = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


  
    for c in cnts_green:
        area1 = cv2.contourArea(c)
        if area1>5000:
            cv2.drawContours(frame, [c], -1, (0,255,0),3)
            cv2.putText(frame, "Access Granted", (20,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),1)

    for c in cnts_red:
        area2 = cv2.contourArea(c)
        if area2>5000:
            cv2.drawContours(frame, [c], -1, (0,255,0),3)
            cv2.putText(frame, "Acess Denied", (20,30), cv2.FONT_HERSHEY_COMPLEX, 1, (255,255,255),2)



    cv2.imshow('Do u have access?', frame)

    k = cv2.waitKey(5)
    if k==27:
        break

cap.release()
cv2.destroyAllWindows()
