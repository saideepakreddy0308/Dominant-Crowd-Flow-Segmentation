#        Streakflow For Crowd Segmentation          #
[![Issues](https://camo.githubusercontent.com/926d8ca67df15de5bd1abac234c0603d94f66c00/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f636f6e747269627574696f6e732d77656c636f6d652d627269676874677265656e2e7376673f7374796c653d666c6174)](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/issues)
[![Say Thanks!](https://img.shields.io/badge/SayThanks.io-%E2%98%BC-1EAEDB.svg)](mailto:saideepakreddy0308@gmail.com)

## Introduction
Dominant crowd flow segmentation is the first step towards building an automated monitoring system for high density crowd scenes. In computer vision, optical flow is widely used to compute pixel wise instantaneous motion between consecutive frames, and numerous methods are reported to efficiently compute accurate optical flow. However, optical flow does not capture long-range temporal dependencies, since it is based on just two frames. In order to achieve an accurate representation of flow from crowd motion, we use the streaklines to compute a new motion field which we refer to as streak flow. To compute streak flow, streaklines are computed by temporally integrating optical flow.

![Block_Diagram](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/blockdiagram.jpg)

## The Motivation
* Crowd Flow Segmentation was conceived as a part of the end semester project for Course - Digital Image Processing.
* The primary motivation however was to know the flow estimation of the crowded scene.

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
[**crowd_flow.py**](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Code_Files/crowd_flow.py) : This script is the main python program which consists of all other scripts namely OpticalFlow, Orientation_Histogram, HeatMap, Watershed algorithms.
  - After installing all the required python packages you can try running the **crowd_flow.py** file to see the output.

#### About other Files/Folders:
- Input video file to all the scripts is **2181-2_70.mov**.
- Project Report.pdf is the project report based on the output results of the python codes.

  > **You can download the report [here](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Project%20Report.pdf)
 
- Screenshots of written-output video are saved in the [Frames](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Frames) directory.
- Results(output is written in .avi/.mp4 format) of the scripts are contained in the [Results](https://github.com/saideepakreddy0308/Dominant-Crowd-Flow-Segmentation/blob/main/Results) directory.

## How to run the code
Go to the Code_Files directory.
Then, 
1. Download the input video file into your local directory.
2. Run the first code with command `python crowd_flow.py` to start tracking.
3. Finish program with `q` or `Esc` key.

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
