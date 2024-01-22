import cv2

video = cv2.VideoCapture(0)
imageNo = 0
savePath = "images/Calibration_images/"

# save captured image 
while True:
    _,frame = video.read()
    cv2.imshow('Frame',frame)  
    if  cv2.waitKey(1) & 0xFF == ord('s'): 
        status = cv2.imwrite(savePath + 'capture{}.jpg'.format(imageNo),frame)
        if status is True:
            print("Saved image.")
            imageNo += 1
        else:
            print("Error occured! Check your image path exists.")
    elif cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

video.release()
cv2.destroyAllWindows()