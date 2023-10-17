#################################################
Blind/Referenceless Image Spatial Quality Evaluator
#################################################

No-Reference Quality Metrics

*********
Description
*********

The Blind/Referenceless Image Spatial Quality Evaluator (BRISQUE) metric is a model that uses only the image pixels to calculate features. It has proven to be extremely efficient as it does not require any transformation to compute its features. BRISQUE relies on the spatial Natural Scene Statistics (NSS) model of locally normalised luminance coefficients in the spatial domain, as well as the model for pairwise products of these coefficients. 

******************
Interpretation
******************

BRISQUE has a score from 1 (Good) - 100 (Poor).

*********
Limits
*********
BRISQUE is trained with an image dataset so its performance and validity heavily depends on the training data.

******************
Example
******************
Images from a traffic surveillance camera in Germany is used to show the BRISQUE results.

Standard image with BRISQUE score 48.74

.. image:: examples/Reference_Image.png
  :width: 640
 
Dark image with BRISQUE score 48.17

.. image:: examples/Image_Dark.png
  :width: 640
  
Dark image with BRISQUE score 51.60

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************


MATLAB
=========
The MATLAB Image Processing Toolbox contains a function to calculate the BRISQUE score:
::
  standard = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  score = brisque(standard);
  fprintf('\nThe BRISQUE score for the standard image %0.4f\n', score);

  score = brisque(dark);
  fprintf('\nThe BRISQUE score for the dark image %0.4f\n', score);

  score = brisque(sun);
  fprintf('\nThe BRISQUE score for the sunny image %0.4f\n', score);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/brisque.html>`_.

C++
=========
OpenCV contains a class for calculating the BRISQUE. A detailed description can be found in the `OpenCV Docs <https://docs.opencv.org/4.x/d8/d99/classcv_1_1quality_1_1QualityBRISQUE.html>`_:
::
  #include <opencv2/quality/qualitybrisque.hpp>
  #include <iostream>

  int main()
  {
    std::string image_path = samples::findFile("Reference_Image.png");
    cv::Mat img_standard = cv::imread(image_path, cv::IMREAD_COLOR);
    std::string image_path = samples::findFile("Image_Dark.png");
    cv::Mat img_dark = cv::imread(image_path, cv::IMREAD_COLOR);
    std::string image_path = samples::findFile("Image_Sunshine.png");
    cv::Mat img_sun = cv::imread(image_path, cv::IMREAD_COLOR);
    
    cv::quality::QualityBRISQUE BRISQUE_standard();
    cv::Scalar BRISQUE_1 = BRISQUE_standard.compute(img_standard);
    
    cv::quality::QualityBRISQUE BRISQUE_dark();
    cv::Scalar BRISQUE_2 = BRISQUE_standard.compute(img_dark);
    
    cv::quality::QualityBRISQUE BRISQUE_sun();
    cv::Scalar BRISQUE_3 = BRISQUE_standard.compute(img_sun);
  }
  
********************
Literature
********************
https://learnopencv.com/image-quality-assessment-brisque/
