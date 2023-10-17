#################################################
Naturalness Image Quality Evaluator
#################################################

No-Reference Quality Metrics

*********
Description
*********

The Natural Image Quality Evaluator (NIQE) metric makes only use of measurable deviations from statistical regularities observed in natural images, without training on human-rated distorted images, and, indeed without any exposure to distorted images. 
It is based on the construction of a quality aware collection of statistical features based on a simple and successful space domain natural scene statistic (NSS) model. These features are derived from a corpus of natural, undistorted images. 

******************
Interpretation
******************

The lower the NIQE value, the better. A NIQE value of 0 is the best.

*********
Limits
*********
NIQE is trained with an image dataset so its performance and validity heavily depends on the training data.

******************
Example
******************
Images from a traffic surveillance camera in Germany is used to show the NIQE results.

Standard image with NIQE score 3.75

.. image:: examples/Reference_Image.png
  :width: 640
 
Dark image with NIQE score 4.64

.. image:: examples/Image_Dark.png
  :width: 640
  
Dark image with NIQE score 3.93

.. image:: examples/Image_Sunshine.png
  :width: 640

********************
Tools and Libraries
********************

Python
=========
There is one `python repository <https://github.com/guptapraful/niqe>`_ implementing NIQE for grayscale images.

MATLAB
=========
The MATLAB Image Processing Toolbox contains a function to calculate the NIQE score:
::
  standard = imread('Reference_Image.png');
  dark = imread('Image_Dark.png');
  sun = imread('Image_Sunshine.png');

  score = niqe(standard);
  fprintf('\nThe NIQE score for the standard image %0.4f\n', score);

  score = niqe(dark);
  fprintf('\nThe NIQE score for the dark image %0.4f\n', score);

  score = niqe(sun);
  fprintf('\nThe NIQE score for the sunny image %0.4f\n', score);

A detailed description can be found at the `Mathworks Website <https://de.mathworks.com/help/images/ref/niqe.html>`_.

  
********************
Literature
********************

http://live.ece.utexas.edu/publications/2012/Asilomar_MicheleSaad.pdf
