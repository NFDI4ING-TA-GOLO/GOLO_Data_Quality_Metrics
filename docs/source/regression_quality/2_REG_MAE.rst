####################################
Mean Absolute Error (MAE)
####################################

************
Description
************

The MAE measures the average magnitude of the errors between predicted and observed values. It's the average of the absolute differences between predictions and actual values. The MAE is defined as:

.. math::
   \text{MAE} = \frac{1}{n} \sum_{i=1}^{n} |y_i - \hat{y}_i|

where:

- \( n \) is the number of observations.
- \( y_i \) is the actual value.
- \( \hat{y}_i \) is the predicted value.

********************
Tools and Libraries
********************

Python
=========

To compute the MAE between the actual values and predicted values, the following example can be used.

Install **scikit-learn** via this command:
:: 
   pip install -U scikit-learn
   
   
.. literalinclude:: examples/REG_MAE/REG_MAE.py

