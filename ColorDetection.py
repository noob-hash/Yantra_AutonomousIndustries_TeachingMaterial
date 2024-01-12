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


def make_decision(coordinates,image_width,color):
    left_region = image_width // 3
    right_region = 2 * (image_width // 3)
    # Define regions for left, center, and right

    if color in ['Blue','R','G']:
        centroid_x = np.mean(coordinates[:, 1])
        if centroid_x < left_region:
            return "L"
        elif centroid_x > right_region:
            return "R"
        else:
            return "F"
    elif color == 'B':
        # to code
        return "B"
    elif color == 'W':
        # to code
        return "F"        

def  find_object(frame):
    width = frame.shape[1]
    red_pixels, green_pixels, blue_pixels, white_pixels, black_pixels = identify_colors(frame)
    decision_red = make_decision(red_pixels,width,'R')
    decision_green = make_decision(green_pixels,width,'G')
    decision_blue = make_decision(blue_pixels,width,'Blue')
    decision_white = make_decision(white_pixels,width,'G')
    decision_black = make_decision(black_pixels,width,'Blue')
    
    return decision_red,decision_green, decision_blue, decision_black, decision_white

vid = cv2.VideoCapture(0)
while True:
    _,frame = vid.read()
    frame = cv2.flip(frame,1)
    decision_red,decision_green, decision_blue, decision_black, decision_white = find_object(frame)
    print("Red pixels:", decision_red,)
    print("Green pixels:", decision_green)
    print("Blue pixels:", decision_blue)
    print("Black pixels:", decision_black)
    print("White pixels:", decision_white)

    cv2.imshow('Frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break 

vid.release()
cv2.destroyAllWindows()