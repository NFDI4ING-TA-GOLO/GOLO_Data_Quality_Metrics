#################################################
Perception based Image Quality Evaluator
#################################################

No-Reference Quality Metrics

*********
Description
*********

The Perception based Image Quality Evaluator (PIQE) metric is opinion-unaware and unsupervised, which means it does not require a trained model. PIQE can measure the quality of images with arbitrary distortion and in most cases performs similar to NIQE. PIQE estimates block-wise distortion and measures the local variance of perceptibly distorted blocks to compute the quality score. (Source: Mathworks)

******************
Interpretation
******************

The lower the PIQE score, the better. A PIQE value of 0 is the best.

*********
Limits
*********

PIQE is less computationally efficient than NIQE or BRISQUE, but it provides local measures of quality in addition to a global quality score.

******************
Example
******************
Images from a traffic surveillance camera in Germany is used to show the PIQE results.

Standard image with PIQE score 72.81

.. image:: examples/Reference_Image.png
  :width: 640
 
Dark image with PIQE score 73.83

.. image:: examples/Image_Dark.png
  :width: 640
  
Dark image with PIQE score 75,73

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************

Python
=========
There is one `python repository <https://github.com/buyizhiyou/NRVQA>`_ implementing PIQE.

MATLAB
=========
The MATLAB Image Processing Toolbox contains a function to calculate the PIQE score:
::
  standard = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  score = piqe(standard);
  fprintf('\nThe PIQE score for the standard image %0.4f\n', score);

  score = niqe(dark);
  fprintf('\nThe PIQE score for the dark image %0.4f\n', score);

  score = niqe(sun);
  fprintf('\nThe PIQE score for the sunny image %0.4f\n', score);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/piqe.html>`_.

  
********************
Literature
********************

https://raiith.iith.ac.in/1527/1/1527_raiith_07084843.pdf
