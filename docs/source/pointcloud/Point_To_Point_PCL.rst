#################################################
Point-to-Point
#################################################

Also referred to as Cloud-to-Cloud distances.

*********
Description
*********

First, for every point in one point cloud, a corresponding point from the other point cloud is identified. Then the average or maximum of the Euclidean distances between such point pairs is used as the basis for a measurement.

******************
Interpretation
******************

The Point-to-Plane requires two point clouds. One reference point cloud and one actual point cloud. Both point clouds has to be recorded within the same environment as well as with the same position, orientation, and parameters.

*********
Limits
*********

Only the noise of the LiDAR, laserscanner or RADAR can be evaluated.

The setup requires a static enviroment, so impacts on the signal quality with a sensor on a moving object can't be evaluated.

******************
Example
******************

Will be added in the future.

********************
Tools and Libraries
********************

The implementation depends on the PCL format. Information to assign the points between the different point cloud are required, e. g. the channel and angle. 

An example will be implemented in the future.

Python
=========

MATLAB
=========

C++
=========


********************
Literature
********************
https://ieeexplore.ieee.org/stamp/stamp.jsp?tp=&arnumber=8296925
