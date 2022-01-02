# Streak Flow and Orientation Histogram
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

# To Draw the Streak Flow
def draw_flow(img, flow, step=9):
    # Height and Width of the Frame
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1).astype(int)
    fx, fy = flow[y, x].T
    lines = np.vstack([x, y, x - fx, y - fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    # Converting the image from GrayScale to BGR
    img_bgr = cv.cvtColor(img, cv.COLOR_GRAY2BGR)
    # Drawing the Streak Lines
    cv.polylines(img_bgr, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        cv.circle(img_bgr, (x1, y1), 1, (0, 255, 0), -1)
    return img_bgr

# Reading the video
cap = cv.VideoCapture('2181-2_70.mov')
# Reading the first frame from the video
# ret, frame = cap.read()
# ret is a boolean variable that returns true if the frame is available.
# frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
ret, prev = cap.read()

# Converting the frame to GrayScale
prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)

# Creating a np array of similar size to the frame
hsv = np.zeros_like(prev)
# hsv.fill(255)
hsv[..., 1] = 255

# We need to set resolutions.so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

# Below VideoWriter object will create a frame of above defined The output is stored in Orientation_Histogram.avi' file.
result = cv.VideoWriter('Orientation_Histogram.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while True:
    # Reading a frame from video
    ret, img = cap.read()
    if not ret:
        print('No frames grabbed!')
        break
    # Create a blank 300x300 black image
    image = np.zeros((300, 300, 3), np.uint8)
    # Fill image with red color(set each pixel to red)
    image[:] = (0, 0, 255)
    # Converting the frame into GrayScale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Computing the flow from the frame
    flow = cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    # Computing the magnitude and angle from the flow
    mag, ang = cv.cartToPolar(flow[..., 0], flow[..., 1])
    hsv[..., 0] = ang * 180 / np.pi / 2
    hsv[..., 2] = cv.normalize(mag, None, 0, 255, cv.NORM_MINMAX)
    # Converting the image from hsv to bgr format
    bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
    # Making the present frame as previous frame
    prevgray = gray

    
    # Write the frame into the file 'StreakFlow.avi'
    result.write(draw_flow(gray, flow))
    # Display the frame saved in the file
    cv.imshow('original', img)
    cv.imshow('Velocity-vectors', draw_flow(gray, flow))
    # Press q on keyboard to stop the process
    key = cv.waitKey(5)
    if key == ord('q'):
        # Break the loop
        break
        
## When everything done, release the video capture and video write objects
cap.release()
result.release()
# Destroying and closes all the windows
cv.destroyAllWindows()
print("The video was successfully saved")