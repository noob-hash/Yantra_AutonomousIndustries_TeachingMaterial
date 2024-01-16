# from BotControl import forward,left,right,backward,all_motor_off
from time import sleep
# from ServoControl import catch,release,cam_back,cam_front
import cv2
import numpy as np
from ColorDetection import identify_colors, color_position

def  find_object(frame):
    width = frame.shape[1]
    red_pixels, green_pixels, blue_pixels, white_pixels, black_pixels = identify_colors(frame)
    position_red = color_position(red_pixels,width)
    position_green = color_position(green_pixels,width)
    position_blue = color_position(blue_pixels,width)
    position_white = color_position(white_pixels,width)
    position_black = color_position(black_pixels,width)
    
    return position_red,position_green, position_blue, position_black, position_white

def make_decision(position_red,position_green, position_blue, position_black, position_white,red_completed, green_completed, blue_completed):
    if red_completed or green_completed or blue_completed:
        print("Aa")
        
    else:
        if not red_completed and position_red != None:
            print("A")

def main():
    vid = cv2.VideoCapture(0)
    red_completed, green_completed, blue_completed = False,False,False

    while True:
        _,frame = vid.read()
        frame = cv2.flip(frame,1)
        position_red,position_green, position_blue, position_black, position_white = find_object(frame)
        decision = make_decision(position_red,position_green, position_blue, position_black, position_white,red_completed, green_completed, blue_completed)
        print("Red pixels:", position_red,decision)
        # print("Green pixels:", position_green)
        # print("Blue pixels:", position_blue)
        # print("Black pixels:", position_black)
        # print("White pixels:", position_white)

        cv2.imshow('Frame',frame)   
        if cv2.waitKey(1) & 0xFF == ord('q'): 
            break 

    vid.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()