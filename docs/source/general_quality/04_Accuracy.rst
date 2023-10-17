####################################
Accuracy
####################################

*********
Description
*********

Data accuracy is a key characteristic of data quality. This metric refers to the fact that values for a specific object are mapped in the correct format and size. This metric is used to
emphasise the correctness and consistency of data and to prevent ambiguity.

If one questions whether the recorded data reflects the real world. Here, 
accuracy can refer to decimal places of decimal numbers or even trivially to the incorrect spelling of names and addresses.

Accuracy can be determined using ground truth, an alternative data recording. Data accuracy can be described by the standard error.

********************
Tools and Libraries
********************

Python
=========

Install **numpy** and **scipy** via command:
:: 
  pip install numpy

  pip install scipy

Using numpy to calculate standard error
---------------------------------------

.. literalinclude:: examples/accuracy/accuracy_func1.py


Using scipy.stats to calculate standard error
--------------------------------------------------------

.. literalinclude:: examples/accuracy/accuracy_func2.py



MATLAB
=========

C++
=========

********************
Literature
********************