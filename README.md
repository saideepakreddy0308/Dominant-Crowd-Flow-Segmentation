#        Streakflow For Crowd Segmentation          #

## The Motivation
* Crowd Flow Segmentation was conceived as a part of the end semester project for Course - Digital Image Processing.
* The primary motivation however was to know the flow estimation of the crowded scene.

# Contributors:
-> Sai Deepak Reddy Kamaganikuntla
-> Chokkari Dinesh
-> Mohit Khushlani
-> Harish Petkar
-> Kumar Pratyay

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
# Requirements

The source code of this project is written in **Python**. So, you'll require **OpenCV/Numpy Libraries and JupyterNotebook/MatLab Platform** to run this project.

## Scripts

1. **OpticalFlow.py** : The motion of video which is within the set of frames, basically the objects might be moving. Now when the objects are moving, they get displaced from its original location. If you simply compute the intensity differences between the frames that also gives you the notion of motion. It tries to capture the displacement of the moving objects. And when we try to represent it in a color coded way we can see different intensity values and what you see in the optical flow or the maximum flow or maximum movement is happening.

2. **Orientation_Histogram.py**  : This script which is also the streakflow representation.It gives the directionality of the motion.The displacement, which is happening between two consecutive frames and taken over the set of frames. This is nothing but an orientation histogram which has been plotted. It previews directionality shown with small small arrows. 

3. **HeatMap.py**  :  Here, which is also showing similarities i.e we find a factors that whether these directionality patterns or some kind of patterns, in the motion, using the peak lines. Another way of showing the maximum of the flow, which is happening.

4. **Watershed.py** : This script shows the  segregating of the flow pattern which we have captured in the similarities.

# About other Files:
- crowd_flow.py is the main python program which consists of all the codes(OpticalFlow,Orientation_Histogram,HeatMap,Watershed algorithms) in different functions.
- project_report.pdf is the project report based on the output results of the python codes.
- After installing all the required python packages you can try running the crowd_flow.py file to see the output.

## How to run the code
Go to the directory.
Then, 
1. Run the first code with command `python crowd_flow.py`
2. Then, press `Enter` key to start tracking.
3. Finish program with `q` or `Esc` key.

## References
* R. Mehran, B. E. Moore, and M. Shah, “A streakline representation of flow in crowded scenes,” in 
  Computer Vision—ECCV 2010: 11th European Conference on Computer Vision, Heraklion, Crete, 
  Greece, September 5–11, 2010, Proceedings, Part III, vol. 6313 of Lecture Notes in Computer 
  Science, pp. 439–452, Springer, Berlin, Germany, 2010.
* https://www.crcv.ucf.edu/projects/streakline_eccv
