#################################################
Multi-Scale Structural Similarity
#################################################

Full-Reference Quality Metrics

*********
Description
*********

The Multi-Scale Structural Similarity (MS-SSIM) metric extends the SSIM index by combining luminance information at the highest resolution level with texture and contrast information at multiple downscaled resolutions or scales. The different scales account for the variability in the perception of image detail caused by factors such as the viewing distance to the image, the distance between the scene and the sensor, and the resolution of the image capture sensor.

******************
Interpretation
******************

When an image has maximal pixel differences , the MS-SSIM equals zero. As image differences decreases, its value increases.

*********
Limits
*********
The smaller der MS-SSIM values the greater the difference between the pixels.

The MS-SSIM can only be calculated for gray scale images. However, if you use RGB image most implementations will treat each channel as an unique gray scale image.

Only images showing the same scene should be compared. 

******************
Example
******************
Images from a traffic surveillance camera in Germany is used to show the MS-SSIM results.

Reference Image

.. image:: examples/Reference_Image.png
  :width: 640
 
The global MS-SSIM score is for the R: 0.768 G: 0.778 B: 0.785

.. image:: examples/Image_Dark.png
  :width: 640
  
The global MS-SSIM score is for the R: 0.887 G: 0.892 B: 0.893

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************

Python
=========
In Python the package **sewar** contains multiple image quality metrics. One of them is the MS-SSIM.

Install package:
:: 
  pip install sewar

Calculate MS-SSIM:
::
  from sewar.full_ref import msssim
  from PIL import Image

  img1 = Image.open('Reference_Image.png')
  img2 = Image.open('Image_Dark.png')
  msssim(img1,img2) 
  

MATLAB
=========
Within the MATLAB Image Processing Toolbox a function to calculate the MS-SSIM exists:
::
  ref = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  score = multissim(dark,ref)
  fprintf('\nThe MS-SSIM score for the dark image %0.4f\n', score);

  score = multissim(dark,ref)
  fprintf('\nThe MS-SSIM score for the sunny image %0.4f\n', score);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/multissim.html>`_.

********************
Literature
********************
