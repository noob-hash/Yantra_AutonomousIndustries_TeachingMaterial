import cv2
import numpy as np
from time import sleep  

# find which of following color exists and where
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

# convert pixel color to where it lies in left, middle or right of screen
def color_position(coordinates,image_width):
    if len(coordinates) == 0:
        return None
    
    left_region = image_width // 3
    right_region = 2 * (image_width // 3)
    # Define regions for left, center, and right

    centroid_x = np.mean(coordinates[:, 1])
    if centroid_x < left_region:
        return "L"
    elif centroid_x > right_region:
        return "R"
    else:
        return "F"


# to make decisions based on the positions of colored objects and data from ultrasonic sensor 1
def make_decision(position_red,position_green, position_blue, position_black, position_white,red_completed, green_completed, blue_completed, dist1):
    if red_completed and green_completed and blue_completed:
        print("Aa")
        
    else:
        if not red_completed and position_red != None:
            return position_red, "R"
        elif not blue_completed and position_blue != None:
            return position_blue, "B"
        elif not green_completed and position_green != None:
            return position_green, "G"
        elif position_red == None and position_green == None and position_blue == None:
            if position_black != 'F':
                if dist1 > 15:
                    return 'F','B'
                else:
                    return 'R','B'
            if position_white == 'F':
                if dist1 > 15:
                    return 'F','W'
                else:
                    return 'R','W'

def main():
    vid = cv2.VideoCapture(0)
    while True:
        _,frame = vid.read()
        frame = cv2.flip(frame,1)
        width = frame.shape[1]
        red_pixels, green_pixels, blue_pixels, white_pixels, black_pixels = identify_colors(frame)
        print("Red:",color_position(red_pixels,width))
        print("Green:",color_position(green_pixels,width))
        print("Blue:",color_position(blue_pixels,width))
        print("White:",color_position(white_pixels,width))
        print("Black:",color_position(black_pixels,width))
        cv2.imshow('Frame',frame)   
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 
        sleep(0.05)

    vid.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()