####################################
Mean Squared Error (MSE)
####################################

************
Description
************

In order to measure the average squared differences between some predicted and actual values, the MSE can be used. 
By squaring the errors before averaging them, larger errors will be penalized. The MSE is defined as follows:

.. math::
   \text{MSE} = \frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2 ,

where:

- \( n \) is the number of observations.
- \( y_i \) is the actual value.
- \( \hat{y}_i \) is the predicted value.


********************
Tools and Libraries
********************

Python
=========

To measure the MSE between the actual values and predicted values, the following example can be used.

Install **scikit-learn** via this command:
:: 
   pip install -U scikit-learn
   
   
.. literalinclude:: examples/REG_MSE/REG_MSE.py



MATLAB
=========

C++
=========

********************
Literature
********************