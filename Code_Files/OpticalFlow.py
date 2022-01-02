# Optical FLow
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

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

# Below VideoWriter object will create a frame of above defined The output is stored in 'OpticalFLow.avi' file.
result = cv.VideoWriter('OpticalFlow.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10, size)

while True:
    # Reading a frame from video
    ret, img = cap.read()
    if not ret:
        print('No frames are grabbed!')
        break
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

    # Write the frame into the file 'OpticalFlow.avi'
    result.write(bgr)
    # Display the frame saved in the file
    cv.imshow('original', img)
    cv.imshow('Dense Optical Flow', bgr)
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