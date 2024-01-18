from BotControl import forward,left,right,backward,all_motor_off
from time import sleep
from ServoControl import catch,release,cam_back,cam_front
import cv2
import numpy as np
from ColorDetection import identify_colors, color_position, make_decision
from DetectShape import find_shape
from ultrasonic import distance1, distance2

#finds the position of different colored objects in the frame
def  find_object(frame):
    width = frame.shape[1]
    red_pixels, green_pixels, blue_pixels, white_pixels, black_pixels = identify_colors(frame)
    position_red = color_position(red_pixels,width)
    position_green = color_position(green_pixels,width)
    position_blue = color_position(blue_pixels,width)
    position_white = color_position(white_pixels,width)
    position_black = color_position(black_pixels,width)
    
    return position_red,position_green, position_blue, position_black, position_white

# main loop of program
def main():
    all_motor_off() # motor is on mtion when pi is off first signal bot to stop

    # capture video from camera
    vid = cv2.VideoCapture(0)
    red_completed, green_completed, blue_completed = False,False,False #determines which tasks are completed
    pick = False #is servo holding something?
    pick_color = None # what color object are we holding
    decision = "S" #trmporary decision can be empty

    while True:
        _,frame = vid.read()
        # frame = cv2.flip(frame,1)
        dist1 = distance1() # data from ultrasonic sensor 1
        dist2 = distance2() # data from ultrasonic sensor 2

        if red_completed and green_completed and blue_completed:
            all_motor_off()
            print("Done")
            break
        else:
            if not pick:
                position_red, position_green, position_blue, position_black, position_white = find_object(frame)
                decision, color = make_decision(position_red,position_green, position_blue, position_black, position_white,red_completed, green_completed, blue_completed, dist1)
                
                if color not in ["B", "W"]:
                    if decision == 'F' and dist1 <= 15:
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
                else:
                    if decision == 'F':
                        forward()
                        sleep(0.5)
                        right()
                        sleep(0.5)
                        all_motor_off()
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
                    elif pick_color == "G":
                        image, decision = find_shape(frame,"Pentagon")
                    elif pick_color == "B":
                        image, decision = find_shape(frame,"Quadrilateral")

                    if decision == 'F' and dist2 <= 15:

                        if pick_color == 'B':
                            blue_completed = True
                        elif pick_color == 'R':
                            red_completed = True
                        elif pick_color == 'G':
                            green_completed = True

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