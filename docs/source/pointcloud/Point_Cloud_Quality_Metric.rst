#################################################
Point Cloud Quality Metric
#################################################


Full-Reference Metric

*********
Description
*********

The Point Cloud Quality Metric (PCQM) is an objective metric for visual quality assessment of colored 3D point clouds. It in an optimally-weighted linear combination of geometry-based and color-based features. It matches color points of an image with PCL points to derive the quality of the PCL points.

******************
Interpretation
******************

The smaller the PCQM score, the better is the quality. A PCQM score of 0 is the best.

*********
Limits
*********

The quality of the results depends on the matching algorithm between 2D image data and the point cloud data. Therefore the quality of the matching has to be evaluated, too.

******************
Example
******************

Will be added in the future.

********************
Tools and Libraries
********************

Python
=========

MATLAB
=========

C++
=========
A C++ implementation by the authors can be found in https://github.com/MEPP-team/PCQM. 

********************
Literature
********************
https://hal.archives-ouvertes.fr/hal-02529668v1
