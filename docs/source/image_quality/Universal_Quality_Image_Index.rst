#################################################
Universal Quality Image Index
#################################################

Full-Reference Quality Metrics

*********
Description
*********

The Universal Quality Image Index (UQI)s created by modeling an image distortion as a combination of loss of correlation, distortion of luminance, and contrast.

******************
Interpretation
******************

The UQI has a range from 0 to 1. An image with a UQI of 1 has a high quality. An image with a lot of distortion will have a low UQI.

*********
Limits
*********
UQI is simple to calculate and align well with the human perception of quality.

Only images showing the same scene should be compared. 

******************
Example
******************
An image from a traffic surveillance camera in Germany is used to show the UQI results.

Reference Image

.. image:: examples/Reference_Image.png
  :width: 640
 

UQI of 0.593

.. image:: examples/Image_Dark.png
  :width: 640
  

UQI of 0.837

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************

Python
=========
In Python the package **sewar** contains multiple image quality metrics. One of them is the UQI.

Install package:
:: 
  pip install sewar

Calculate UQI:
::
  from sewar.full_ref import uqi
  import cv2

  img_ref = cv2.imread('Reference_Image.png')
  img_dark = cv2.imread('Image_Dark.png')
  img_sun= cv2.imread('Image_Sunshine.png')

  score_dark = uqi(img_ref,img_dark)
  print("Score of dark image", score_dark)

  score_sun = uqi(img_ref,img_sun)
  print("Score of dark image", score_sun)
 
  
********************
Literature
********************
https://ieeexplore.ieee.org/document/995823
