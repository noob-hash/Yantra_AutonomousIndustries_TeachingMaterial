from BotControl import forward,left,right,backward,all_motor_off
from time import sleep
from ServoControl import catch,release,cam_back,cam_front
import cv2
import numpy as np


def make_decision(coordinates,image_width,color):
    left_region = image_width // 3
    right_region = 2 * (image_width // 3)
    # Define regions for left, center, and right

    red_completed, green_completed, blue_completed = False

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

def main():
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

if __name__== "__main__":
    main()