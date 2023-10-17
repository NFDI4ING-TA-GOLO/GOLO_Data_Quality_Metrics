####################################
Timeliness and Punctuality
####################################

*********
Description
*********

All data sets must correspond to the desired current state of the depicted reality.
If, in order to answer the research question, data is needed that is current in time.

If not up to date or out of date, this can have very strong negative effects on the results.
Data that may have been up to date last month could be useless now. 

For example, machine learning models trained on old datasets can produce erroneous results or
lead researchers to incorrect conclusions.

To measure timeliness, you may take a small sample of “golden records” for which you have the current value.



********************
Tools and Libraries
********************

Unfortunately, there are no technical tools to determine whether a dataset is up-to-date or not.
However, by declaring minimum and maximum times in which a dataset has been updated, a certain quality can be maintained.

The timeliness of data can be on different levels. The creation date of a file alone can be an indication of whether data is old or young.
This information can usually be obtained from the metadata.

Python
=========

Whether a file is up-to-date can be defined in several ways.
On the one hand, the date of creation of the file can be a more or less good indicator. 
To be able to check the actuality better, data from the file should be compared with data from the real world. If these match, one can assume that the file is up to date.

To check the metadata we need to import the packages os (Operationsystem) and time.

.. literalinclude:: examples/timeliness/func1.py

A better way to measure the timeliness of data is to look at parts of the dataset and compare real-time data. 


MATLAB
=========

C++
=========

********************
Literature
********************