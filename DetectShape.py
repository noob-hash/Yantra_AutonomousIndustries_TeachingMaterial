import cv2

# find and classify shapes in the image
def find_shape(image, target_shape):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY) # threshold to get a binary image
    width = image.shape[1]
    
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    i = 0
    x,y = None, None
    for contour in contours:
        if i == 0:
            i = 1
            continue
        
        # determine approximate position of contours
        approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour, True), True)
        M = cv2.moments(contour)
        x = 0
        y = 0

        if M['m00'] != 0.0:
            x = int(M['m10'] / M['m00'])
            y = int(M['m01'] / M['m00'])

        shape_name = ""
        if len(approx) == 3:
            shape_name = "Triangle"
        elif len(approx) == 4:
            shape_name = "Quadrilateral"
        elif len(approx) == 5:
            shape_name = "Pentagon"
        elif len(approx) == 6:
            shape_name = "Hexagon"
        else:
            shape_name = "Circle"

        if shape_name.lower() == target_shape.lower():
            # we only need position of shape we are searchng for
            # not necessary not here for visualization (down)
            cv2.drawContours(image, [approx], 0, (0, 255, 0), 2)
            cv2.putText(image, shape_name, (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
    
    position = shape_position(x, width)
    return image, position

# determine the position of the detected shape
def shape_position(x, image_width):
    
    if x is None:
        return None
    left_region = image_width // 3
    right_region = 2 * (image_width // 3)
    # Define regions for left, center, and right

    if x < left_region:
        return "L"
    elif x > right_region:
        return "R"
    else:
        return "F"

# Main function for capturing video and detecting shapes
# on;y runs if this program is run as main code
def main():
    vid = cv2.VideoCapture(0)

    while True:
        _, frame = vid.read()
        frame = cv2.flip(frame, 1)
        target_shape = "Quadrilateral"

        detected_shape, position = find_shape(frame, target_shape)
        print(position)
        cv2.imshow('Frame', detected_shape)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    vid.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    main()