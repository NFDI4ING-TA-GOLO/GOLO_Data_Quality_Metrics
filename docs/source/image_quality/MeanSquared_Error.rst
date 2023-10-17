####################################
Mean Squared Error
####################################

Full-Reference Quality Metrics

Also referred to as Mean Squared Deviation (MSD).

*********
Description
*********

The Mean Squared Error (MSE) measures the average squared difference between actual and ideal pixel values. It therefore compares an ideal reference image with an actual image.

******************
Interpretation
******************

When an image has no pixel differences (no errors), the MSE equals zero. As image differences increase, its value increases.

*********
Limits
*********
MSE is simple to calculate but might not align well with the human perception of quality.

Furthermore, the Mean Squared Error depends heavily on the scaling of the image intensity. A mean square error of 100.0 for an 8-bit image (with pixel values in the range 0-255) looks terrible; but an MSE of 100.0 for a 10-bit image (pixel values in the range [0,1023]) is hardly noticeable.

Only images showing the same scene should be compared. 

******************
Example
******************
An image from a traffic surveillance camera in Germany is used to show the MSE results.

Reference Image

.. image:: examples/Reference_Image.png
  :width: 640
 

MSE of 2075.3

.. image:: examples/Image_Dark.png
  :width: 640
  

MSE of 917.8

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************

Python
=========
In Python the package **sewar** contains multiple image quality metrics. One of them is the MSE.

Install package:
:: 
  pip install sewar

Calculate MSE:
::
  from sewar.full_ref import mse
  import cv2

  img_ref = cv2.imread('Reference_Image.png')
  img_dark = cv2.imread('Image_Dark.png')
  img_sun= cv2.imread('Image_Sunshine.png')

  score_dark = mse(img_ref,img_dark)
  print("Score of dark image", score_dark)

  score_sun = mse(img_ref,img_sun)
  print("Score of dark image", score_sun)
 

MATLAB
=========
Within the MATLAB Image Processing Toolbox a function to calculate the MSE exists:
::
  ref = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  MSE_dark = immse(dark, ref);
  fprintf('The mean-squared error for the dark image is %0.4f\n', MSE_dark);

  MSE_sun = immse(sun, ref);
  fprintf('The mean-squared error for the sun image is %0.4f\n', MSE_sun);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/immse.html>`_. For an RGB image the MSE for each channel is calculated and the average of all channel MSEs is the MSE of the image. It is also possible to only calculate the MSE for one channel:
:: 
  ref = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  MSE_R = immse(dark(:,:,1), ref(:,:,1));
  MSE_G = immse(dark(:,:,2), ref(:,:,2));
  MSE_B = immse(dark(:,:,3), ref(:,:,3));
  fprintf('\nThe mean-squared error for R-channel %0.4f\n', MSE_R);
  fprintf('The mean-squared error for G-channel %0.4f\n', MSE_G);
  fprintf('The mean-squared error for B-channel %0.4f\n', MSE_B);
  
If access to the MATLAB Image Processing Toolbox is denied, one can program the MSE by their own:
::
  num_pixel = size(ref,1)*size(ref,2)*size(ref,3);
  MSE = sum((double(ref) - double(dark)).^2,'all') / num_pixel;
  fprintf('The mean-squared error for the dark image is %0.4f\n', MSE);

C++
=========
OpenCV contains a class for calculating the MSE. A detailed description can be found in the `OpenCV Docs <https://docs.opencv.org/4.x/d7/d80/classcv_1_1quality_1_1QualityMSE.html#a82ba740a06f48562a08517079712218c>`_:
::
  #include <opencv2/quality/qualitymse.hpp>
  #include <iostream>

  int main()
  {
    std::string image_path = samples::findFile("Reference_Image.png");
    cv::Mat img_ref = cv::imread(image_path, cv::IMREAD_COLOR);
    std::string image_path = samples::findFile("Image_Dark.png");
    cv::Mat img_dark = cv::imread(image_path, cv::IMREAD_COLOR);
  
    
    cv::quality::QualityMSE::QualityMSE MSE_ref(img_ref);

    cv::Scalar MSE;
    MSE = MSE_ref.compute(img_dark);
  }
  
********************
Literature
********************
https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/VELDHUIZEN/node18.html 

https://homepages.inf.ed.ac.uk/rbf/CVonline/LOCAL_COPIES/VELDHUIZEN/node18.html
