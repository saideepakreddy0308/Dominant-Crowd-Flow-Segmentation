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

def watershed(img):
    #Reading image using cv libraries
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV+cv.THRESH_OTSU)
    # Noise Removal
    kernel = np.ones((3,3),np.uint8)
    opening = cv.morphologyEx(thresh,cv.MORPH_OPEN,kernel, iterations = 2)
    # Background area 
    sure_bg = cv.dilate(opening,kernel,iterations=3)
    # Foreground area
    dist_transform = cv.distanceTransform(opening,cv.DIST_L2,5)
    ret, sure_fg = cv.threshold(dist_transform,0.7*dist_transform.max(),255,0)
    # Finding unknown region
    sure_fg = np.uint8(sure_fg)
    unknown = cv.subtract(sure_bg,sure_fg)
    # Marker labelling
    ret, markers = cv.connectedComponents(sure_fg)
    #Applying watershed algorithm and marking the regions segmented
    markers = markers+1
    markers[unknown==255] = 0
    markers = cv.watershed(img,markers)
    img[markers == -1] = [0,255,255]
    #Displaying the segmented image
    imS = cv.resize(img, (612, 368))
    return imS

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
suc, prev = cap.read()
# suc, frame = cap.read()
# suc is a boolean variable that returns true if the frame is available.
# frame is an image array vector captured based on the default frames per second defined explicitly or implicitly
# Converting the frame to GrayScale
prevgray = cv.cvtColor(prev, cv.COLOR_BGR2GRAY)
# Creating a np array of similar size to the frame
hsv = np.zeros_like(prev)
hsv[..., 1] = 255
# hsv.fill(255)
heat_map = np.zeros(prev.shape[:-1])

while True:
    # Reading a frame from video
    suc, img = cap.read()
    if not suc:
        print('No frames!')
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

    # Display the frame saved in the file
    cv.imshow('original', img)
    cv.imshow('Dense Optical Flow', bgr)
    cv.imshow('Velocity-vectors', draw_flow(gray, flow))
    cv.imshow("Heat Map", img_mapped) 
    cv.imshow('Segmented Result - Watershed', watershed(img_contours))
    
    # Press q on keyboard to stop the process
    key = cv.waitKey(5)
    if key == ord('q'):
        # Break the loop
        break
        
## When everything done, release the video capture.
# Destroying and closes all the windows
cv.destroyAllWindows()
