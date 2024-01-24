import cv2
import json
import numpy as np

# notice that the distortation data is for webcam 
# as such correction might not show real correction in your camera
video = cv2.VideoCapture(0)
camFile = "images/files/camera.json"

with open(camFile, 'r') as json_file:
	camera_data = json.load(json_file)
dist = np.array(camera_data["dist"])
mtx = np.array(camera_data["mtx"])

if video.isOpened():
    while True:
        _, frame = video.read()
        undistorted_frame = cv2.undistort(frame, mtx, dist)

        cv2.imshow('Without Correction', frame)

        cv2.imshow('After Correction', undistorted_frame)

        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 

    video.release()
    cv2.destroyAllWindows()
else:
     print("Error! Check camera connection")