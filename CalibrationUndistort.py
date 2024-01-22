import numpy as np
import cv2
import glob
import json

# Load camera calibration parameters from the JSON file
with open('images/files/camera.json', 'r') as json_file:
    camera_data = json.load(json_file)

# Extract distortion coefficients and camera matrix from the loaded data
dist = np.array(camera_data["dist"])
mtx = np.array(camera_data["mtx"])

# Find images for undistortion
images = glob.glob('images/Calibration_tests/test*.jpg')
print(len(images), "images found")

# Ensure there are images for undistortion
assert len(images) > 0

# Read the first image to get its dimensions
frame = cv2.imread(images[0])
h, w = frame.shape[:2]

# Get the optimal new camera matrix and region of interest (ROI) for undistortion
newCamera_mtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w, h), 0, (w, h))
x, y, w1, h1 = roi
yh1 = y + h1
xw1 = x + w1

# Loop through each image for undistortion
for num, fileName in enumerate(images):
    img = cv2.imread(fileName)

    # Undistort the image using the new camera matrix
    dst = cv2.undistort(img, mtx, dist, None, newCamera_mtx)

    # Crop the image to the region of interest (ROI)
    dst = dst[y:yh1, x:xw1]

    # Display the undistorted image and save it
    cv2.imshow('img', dst)
    cv2.imwrite(f"images/Calibration_undistorted/remapped{num}.jpg", dst)
    cv2.waitKey(1500)
