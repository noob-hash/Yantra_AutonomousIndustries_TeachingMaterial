import numpy as np
import cv2
import glob
import json

# Define termination criteria for the iterative algorithm
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Define the number of rows and columns on the chessboard
rows = 7
columns = 7

# Create 3D object points for the chessboard corners
objp = np.zeros((rows*columns, 3), np.float32)
objp[:, :2] = np.mgrid[0:columns, 0:rows].T.reshape(-1, 2)

# Lists to store object points and image points from all images
objpoints = []
imgpoints = []

# Read images from the specified directory
images = glob.glob('images/Calibration_images/*.jpg')
print(len(images), "images found")

# Loop through each image for calibration
for num, fileName in enumerate(images):
    # Read the image and convert it to grayscale
    img = cv2.imread(fileName)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Flags for chessboard corner detection
    chessboard_flags = cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE

    # Find chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, (columns, rows), chessboard_flags)

    # If corners are found, refine them and store the object and image points
    if ret == True:
        objpoints.append(objp)
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners)

        # Draw and display the corners on the image for visualization
        cv2.drawChessboardCorners(img, (columns, rows), corners2, ret)
        cv2.imshow('img', img)
        cv2.imwrite(f"images/Calibration_tests/test{num}.jpg", img)
        cv2.waitKey(1500)

# Calibrate the camera using the collected object and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# Create a dictionary to store camera calibration parameters
camera = {}

# Custom JSON encoder to handle NumPy arrays
class NumpyEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)

# Store calibration parameters in the dictionary
for variable in ['ret', 'mtx', 'dist', 'rvecs', 'tvecs']:
    camera[variable] = eval(variable)

# Save the camera calibration parameters to a JSON file
with open("images/files/camera.json", 'w') as f:
    json.dump(camera, f, indent=4, cls=NumpyEncoder)

# Close all Opencv2 windows
cv2.destroyAllWindows()
