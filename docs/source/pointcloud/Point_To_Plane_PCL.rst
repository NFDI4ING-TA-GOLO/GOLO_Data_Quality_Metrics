#################################################
Point-to-Plane
#################################################

Also referred to as Cloud-to-Plane.

*********
Description
*********

The intrinsic resolution of the point clouds is proposed as a normalizer to convert the mean square errors to pean-signal noise ratio numbers. 

******************
Interpretation
******************

The Point-to-Plane requires a large plane to have as many points as possible for reference.  

*********
Limits
*********

The quality of the results depends on

- the surface quality of the plane
- knowledge about the position and orientation of the plane

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
The Point Cloud Libray (PCL) provides a GitHub repository to find planes in a point cloud. However, the quality assesment part is missing. A program has to be written to implement the point-to-plane metric.

********************
Literature
********************
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8296925
