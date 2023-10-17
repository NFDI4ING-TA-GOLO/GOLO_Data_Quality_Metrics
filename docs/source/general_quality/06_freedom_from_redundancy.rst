####################################
Freedom from redundancy
####################################

*********
Description
*********

It is essential to identify duplicate data, which can be extremely difficult. With numerical measurement data,
it is almost impossible to identify duplicate numbers.
Therefore, it is better to compare complete data series and decide individually if it is a duplicate recording. 

********************
Tools and Libraries
********************

Python
=========

The pandas.DataFrame.duplicated() method is used to find duplicate rows in a DataFrame.
It returns a boolean series which identifies whether a row is duplicate or unique.

.. literalinclude:: examples/ffr/ffr_func1.py


MATLAB
=========

C++
=========

********************
Literature
********************