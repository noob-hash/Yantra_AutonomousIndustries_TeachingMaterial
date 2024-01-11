import cv2
import numpy as np



vid = cv2.VideoCapture(0)
while True:
    _,frame = vid.read()
    frame = cv2.flip(frame,1) #flip to original
    
    cv2.imshow('Frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

vid.release()
cv2.destroyAllWindows()