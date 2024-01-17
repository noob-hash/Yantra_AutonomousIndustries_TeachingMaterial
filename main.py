from BotControl import forward,left,right,backward,all_motor_off
from time import sleep
from ServoControl import catch,release,cam_back,cam_front
import cv2
import numpy as np
from ColorDetection import identify_colors, color_position
from DetectShape import find_shape
from ultrasonic import distance1, distance2

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
    if red_completed and green_completed and blue_completed:
        print("Aa")
        
    else:
        if not red_completed and position_red != None:
            return position_red, "R"
        elif not blue_completed and position_blue != None:
            return position_blue, "B"
        elif not green_completed and position_green != None:
            return position_green, "G"
        return [],'S'

def main():
    vid = cv2.VideoCapture(0)
    red_completed, green_completed, blue_completed = False,False,False
    pick = False
    pick_color = None
    decision = "S"
    while True:
        _,frame = vid.read()
        frame = cv2.flip(frame,1)
        dist1 = distance1()
        dist2 = distance2()

        if red_completed and green_completed and blue_completed:
            all_motor_off()
            print("Done")
            break
        else:
            if not pick:
                position_red, position_green, position_blue, position_black, position_white = find_object(frame)
                decision, color = make_decision(position_red,position_green, position_blue, position_black, position_white,red_completed, green_completed, blue_completed)
                
                if decision == 'F' and dist1 <= 30:
                    pick_color = color
                    print("Picked:",pick_color)
                    pick = True
                    all_motor_off()
                    catch()
                    cam_back()
                    sleep(2)
                else:
                    if decision == 'F':
                        forward()
                    elif decision == 'L':
                        left()
                    elif decision == 'R':
                        right()
                    elif decision == 'S':
                        all_motor_off()
                print("Find Decision:",decision)

            else:
                if pick_color != None:
                    if pick_color == "R":
                        image, decision = find_shape(frame,"Triangle")
                        red_completed = True
                    elif pick_color == "G":
                        image, decision = find_shape(frame,"Pentagon")
                        green_completed = True
                    elif pick_color == "B":
                        image, decision = find_shape(frame,"Quadrilateral")
                        blue_completed = True

                    if decision == 'F' and dist2 <= 30:
                        print("Completed list(R,G,B):",red_completed,green_completed,blue_completed)
                        all_motor_off()
                        release()  
                        cam_front()
                        pick = False
                        pick_color = None
                        sleep(2)
                    else:
                        if decision == 'F':
                            backward()
                        elif decision == 'L':
                            right()
                        elif decision == 'R':
                            left()
                        elif decision == 'S':
                            all_motor_off()
                print("Picked Decision",decision)
        
        # enable if you need visualization
        # cv2.imshow('Frame',frame)   
        # if cv2.waitKey(1) & 0xFF == ord('q'): 
        #     break 

    vid.release()
    cv2.destroyAllWindows()

if __name__== "__main__":
    main()