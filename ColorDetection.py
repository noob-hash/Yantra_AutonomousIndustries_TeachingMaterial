import cv2
import numpy as np
from ultrasonic import distance1,distance2

def identify_colors(frame):
    # Define color ranges
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    lower_green = np.array([40, 100, 100])
    upper_green = np.array([80, 255, 255])

    lower_blue = np.array([90, 100, 100])
    upper_blue = np.array([130, 255, 255])

    lower_white = np.array([0, 0, 200])
    upper_white = np.array([255, 30, 255])

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 30])

    # Convert frame to HSV
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Create masks for each color
    mask_red = cv2.inRange(hsv_image, lower_red, upper_red)
    mask_green = cv2.inRange(hsv_image, lower_green, upper_green)
    mask_blue = cv2.inRange(hsv_image, lower_blue, upper_blue)
    mask_white = cv2.inRange(hsv_image, lower_white, upper_white)
    mask_black = cv2.inRange(hsv_image, lower_black, upper_black)

    # Get pixel coordinates for each color
    red_pixels = np.column_stack(np.where(mask_red > 0))
    green_pixels = np.column_stack(np.where(mask_green > 0))
    blue_pixels = np.column_stack(np.where(mask_blue > 0))
    white_pixels = np.column_stack(np.where(mask_white > 0))
    black_pixels = np.column_stack(np.where(mask_black > 0))

    return red_pixels, green_pixels, blue_pixels, white_pixels, black_pixels
