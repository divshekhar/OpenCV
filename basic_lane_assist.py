import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def lanesDetectionNew(img):
    # Get the height and width of the provided video frame
    height = img.shape[0]
    width = img.shape[1]

    # Set the image region on witch the lane detection should work
    #ToDo: Make this configurable
    region_of_interest_vertices = [
        (200, height-1), (width/2, height/1.26), (width-400, height-1)
    ]

    # Convert frame to grayscale
    gray_img = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
    # Convert grayscale image to outline borders of objects
    edge = cv.Canny(gray_img, 50, 100, apertureSize=3)

    # Crops the image to the desired region, not sure how exactly this works
    cropped_image = region_of_interest(
        edge, np.array([region_of_interest_vertices], np.int32))
    # Use OpenCVs HoughsLines line detection
    # See https://learnopencv.com/hough-transform-with-opencv-c-python/ for more Info
    lines = cv.HoughLinesP(cropped_image, rho=2, theta=np.pi/180,
                           threshold=40, lines=np.array([]), minLineLength=25, maxLineGap=60)
    # Draw the detected Lines into the original frame
    image_with_lines = draw_lines(img, lines)

    return image_with_lines


def region_of_interest(img, vertices):

    mask = np.zeros_like(img)
    # channel_count = img.shape[2]
    match_mask_color = (255)
    cv.fillPoly(mask, vertices, match_mask_color)
    masked_image = cv.bitwise_and(img, mask)
    return masked_image


def draw_lines(img, lines):
    # Creates a copy of the original image
    img = np.copy(img)
    # Creates a blank image with the dimensions of of the original image
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), np.uint8)

    # Draw the found Lanes as lines onto the blank image
    # Adds color for Lines, to see if the driver is in the middle of the lane
    # Values are tweaked for the specific provided sample video
    for line in lines:
        for x1, y1, x2, y2 in line:
            print("x1: "+str(x1)+" y1: "+str(y1)+" x2: "+str(x2)+" y2: "+str(y2))
            if x1 < 380:
                rgb = (0, 255, 0)
            elif x1 > 700:
                rgb = (0, 255, 0)
            else:
                rgb = (0, 0, 255)
            cv.line(blank_image, (x1, y1), (x2, y2), rgb, 2)

    # Create an image that overlays the blank image with lines onto the original frame
    img = cv.addWeighted(img, 0.8, blank_image, 1, 0.0)
    return img


def videoLanes():
    # Load the Videofile
    cap = cv.VideoCapture('./img/Lane.mp4')
    while(cap.isOpened()):
        # Read one frame from the videofile
        ret, frame = cap.read()
        # Do the lane Detection
        frame = lanesDetectionNew(frame)
        # Display the frame with drawn lanes
        cv.imshow('Lanes Detection', frame)
        # Quit program if q is pressed. cv.waitkey(1) is needed to display something with OpenCV
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    # Close the videofile
    cap.release()
    # Close all OpenCV windows
    cv.destroyAllWindows()


if __name__ == "__main__":
    videoLanes()
