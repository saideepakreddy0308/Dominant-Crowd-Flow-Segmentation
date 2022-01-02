#        Streakflow For Crowd Segmentation          #
[![GitHub license](https://img.shields.io/github/license/saideepakreddy0308/DIP_Project)](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/LICENSE)
[![GitHub repo size](https://img.shields.io/github/repo-size/saideepakreddy0308/DIP_Project.svg?logo=github&style=social)](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation)
[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/saideepakreddy0308/DIP_Project.svg?logo=git&style=social)](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation)
[![Issues](https://camo.githubusercontent.com/926d8ca67df15de5bd1abac234c0603d94f66c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/issues)
[![Say Thanks!](https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg)](mailto:saideepakreddy0308@gmail.com)

## Introduction
Dominant crowd flow segmentation is the first step towards building an automated monitoring system for high density crowd scenes. In computer vision, optical flow is widely used to compute pixel wise instantaneous motion between consecutive frames, and numerous methods are reported to efficiently compute accurate optical flow. However, optical flow does not capture long-range temporal dependencies, since it is based on just two frames. In order to achieve an accurate representation of flow from crowd motion, we use the streaklines to compute a new motion field which we refer to as streak flow. To compute streak flow, streaklines are computed by temporally integrating optical flow.

![Block_Diagram](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/blockdiagram.jpg)

## The Motivation
* Crowd Flow Segmentation was conceived as a part of the end semester project for Course - Digital Image Processing.
* The primary motivation however was to know the flow estimation of the crowded scene.

## Contributors:
- Sai Deepak Reddy Kamaganikuntla ( [https://github.com/saideepakreddy0308](https://github.com/saideepakreddy0308) )
- Chokkari Dinesh
- Mohit Khushlani
- Harish Petkar
- Kumar Pratyay

## Requirements
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![OpenCV](https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white)
![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)
![PyCharm](https://img.shields.io/badge/pycharm-143?style=for-the-badge&logo=pycharm&logoColor=black&color=black&labelColor=green)

The source code of this project is written in **Python**. So, you'll require **OpenCV/Numpy Libraries and JupyterNotebook/MatLab Platform** to run this project.

## Dependencies
- Python 3.9.9, [OpenCV](https://opencv.org/)
- Hit the following Python Libraries Required  in CMD/Terminal if you don't have already them installed:
  * OpenCV
      ```bash
      pip install opencv-python
      ```
  * Numpy
      ```bash
      pip install numpy
      ```
  * MatplotLib
      ```bash
      pip install matplotlib
      ```  

## Scripts

1. [**crowd_flow.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/crowd_flow.py) : This script is the main python program which consists of all other scripts namely OpticalFlow, Orientation_Histogram, HeatMap, Watershed algorithms.
  - After installing all the required python packages you can try running the **crowd_flow.py** file to see the output.

2. [**OpticalFlow.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/OpticalFlow.py) : This script is about Optical flow. Optical flow is the pattern of apparent motion of image objects between two consecutive frames caused by the movement of objects or camera. It is shown in a 2D vector field where each vector is a displacement vector showing the movement of points from first frame to second.The algorithm we use for visualizing Optical flow in our dataset is the farneback algorithm which needs a 1D input image and then use the function cv.calcOpticalFlowFarneback().Direction corresponds to Hue value of the image. Magnitude corresponds to Value plane.

3. [**Orientation_Histogram.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/Orientation_Histogram.py)  : This script which is about the streakflow representation. It gives the directionality of the motion. This is nothing but an orientation histogram which has been plotted. It previews directionality shown with small small arrows.Streaklines are obtained by repeatedly initializing a fixed grid of particles at each frame, then moving both current and past particles using optical flow. This leads to a representation of the flow that more accurately recognizes spatial and temporal changes in the scene, compared with other commonly used flow representations. Streaklines are instantaneous and capture the continuity of motion. Based upon computation by streaklines, streakflow is an instantaneous vector field which represents the accumulative motion of the scene. It resembles the temporal average of optical flow but it is more imminent. Streakflow relates to group motion, instantaneously reacts to changes and has far less noise than optical flow. We show streakflow using the functions cv.polylines() and cv.circle().

4. [**HeatMap.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/HeatMap.py)  :  This script is showing the similarities i.e we find a factors that whether these directionality patterns or some kind of patterns in the motion, using the peak lines. It is another way of showing the maximum of the flow happening. We compare the similarities between adjacent frames of the video and get a heatmap as an output to show the flow segments in the sequence and show the dynamic potential flows with color coded regions for divergent and convergent regions. To define accurate boundaries we do it with the help of cv.dilate() and cv.erode(). Color coded using cv.applyColorMap() and final function used is cv.drawContours(). 

5. [**Watershed.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/Watershed.py) : This script shows the segregating of the flow pattern which we have captured in the similarities. In OpenCV we have a marker-based watershed algorithm where you specify which are all valley points are to be merged and which are not. In every frame of our sequence, we give different labels for our object we know. Label the region which we are sure of being the foreground or object with one color, label the region which we are sure of being background or non-object with another color and finally the region which we are not sure of anything, label it with 0. That is our marker and Then apply watershed algorithm. Our marker then will be updated with the labels we gave, and the boundaries of objects will have a value of -1.
Morphological opening and closing is used to remove white noise and holes respectively. cv.dilate() is used to increase object boundary to the background. Other important functions we use in our code are cv.connectedComponents() (for markers) as well as cv.watershed() (to get the final watershed segmentation). 

#### About other Files/Folders:
- Project Report.pdf is the project report based on the output results of the python codes.

  > **You can download the report [here](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Project%20Report.pdf)
 
- Screenshots of written-output video are saved in the [Frames](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Frames) directory.
- Results(output is written in .avi format) of the scripts are contained in the [Results](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Results) directory.

## How to run the code
Go to the Code_Files directory.
Then, 
1. Run the first code with command `python crowd_flow.py` to start tracking.
2. Finish program with `q` or `Esc` key.

## References
* R. Mehran, B. E. Moore, and M. Shah, “A streakline representation of flow in crowded scenes,” in 
  Computer Vision—ECCV 2010: 11th European Conference on Computer Vision, Heraklion, Crete, 
  Greece, September 5–11, 2010, Proceedings, Part III, vol. 6313 of Lecture Notes in Computer 
  Science, pp. 439–452, Springer, Berlin, Germany, 2010.
* https://www.crcv.ucf.edu/projects/streakline_eccv

## License
This project is available under the MIT license. See the [LICENSE File](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/LICENSE) for more info.

#### Connect with me on :
<a href="https://www.linkedin.com/in/sai-deepak-reddy-k/">
  <img align="left" alt="Deepak's LinkedIn" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/linkedin.svg" />
</a>
<a href="https://github.com/saideepakreddy0308">
  <img align="left" alt="Deepak's Github" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/github.svg" />
</a>
<!-- <a href="link">
  <img align="left" alt="Deepak's Instagram" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/instagram.svg" />
</a>
<a href="link">
  <img align="left" alt="Deepak's Hackerrank" width="22px" src="https://cdn.jsdelivr.net/npm/simple-icons@v3/icons/hackerrank.svg" />
</a> -->
<br><br>
