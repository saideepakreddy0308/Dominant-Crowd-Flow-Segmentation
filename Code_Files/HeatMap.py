# HeatMap
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def process(img):
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_blur = cv.GaussianBlur(img_gray, (5, 5), 25)
    img_canny = cv.Canny(img_blur, 5, 50)
    kernel = np.ones((3, 3))
    img_dilate = cv.dilate(img_canny, kernel, iterations=4)
    img_erode = cv.erode(img_dilate, kernel, iterations=1)
    return img_erode

def get_contours(img, img_original):
    img_contours = img_original.copy()
    contours, hierarchies = cv.findContours(img, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

    cv.drawContours(img_contours, contours, -1, (0, 255, 0), -1) 
    # If you want to omit smaller contours, loop through the detected contours, and only draw them on the image if they are at least a specific area. Don't forget to remove the line above if you choose the below block of code.
    # for cnt in contours: 
    #     if cv2.contourArea(cnt) > 500:
    #         cv2.drawContours(img_contours, [cnt], -1, (0, 255, 0), -1) 
    return img_contours
# Reading the video
cap = cv.VideoCapture('2181-2_70.mov')
# Reading the first frame from the video
suc, prev = cap.read()
# ret, frame = cap.read()
# ret is a boolean variable that returns true if the frame is available.
# frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
# Converting the frame to GrayScale
prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
# Creating a np array of similar size to the frame
hsv = np.zeros_like(prev)
hsv[..., 1] = 255
# hsv.fill(255)
heat_map = np.zeros(prev.shape[:-1])

# We need to set resolutions.so, convert them from float to integer.
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
size = (frame_width, frame_height)

# Below VideoWriter object will create a frame of above defined The output is stored in 'HeatMap.avi' file.
result = cv.VideoWriter('HeatMap.avi', 
                         cv.VideoWriter_fourcc(*'MJPG'),
                         10, size)
while True:
    # Reading a frame from video
    suc, img = cap.read()
    if not suc:
        print('No frames grabbed!')
        break
    # Create a blank 300x300 black image
    image = np.zeros((300, 300, 3), np.uint8)
    # Fill image with red color(set each pixel to red)
    image[:] = (0, 0, 255)

    # Converting the frame into GrayScale
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    #HeatMap
    diff = cv.absdiff(prev, img)
    img_contours = get_contours(process(diff), prev)
    heat_map[np.all(img_contours == [0, 255, 0], 2)] += 3 # The 3 can be tweaked depending on how fast you want the colors to respond
    heat_map[np.any(img_contours != [0, 255, 0], 2)] -= 3
    heat_map[heat_map < 0] = 0
    heat_map[heat_map > 255] = 255
    #  img[heat_map > 160] = img_mapped[heat_map > 160] Use this line to draw the heat map on the original video at a specific temperature range.
    #  For this it's where ever the temperature is above 160 (min is 0 and max is 255)
    img_mapped = cv.applyColorMap(heat_map.astype('uint8'), cv.COLORMAP_JET)

    # Making the present frame as previous frame
    prevgray = gray

    # Write the frame into the file 'HeatMap.avi'
    result.write(img_mapped)
     # Display the frame saved in the file
    cv.imshow('original', img)
    cv.imshow("Heat Map", img_mapped) 
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