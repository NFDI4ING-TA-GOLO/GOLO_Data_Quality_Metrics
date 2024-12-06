####################################
Root Mean Squared Error (RMSE)
####################################

************
Description
************
While MSE is measured in units that are the square of the target value, the RMSE delivers the size of the error in the same units as the original data. RMSE is easier to interpret than MSE, which is why it's more commonly used.

.. math::
   \text{RMSE} = \sqrt{\frac{1}{n} \sum_{i=1}^{n} (y_i - \hat{y}_i)^2}

where:

- \( n \) is the number of observations.
- \( y_i \) is the actual value.
- \( \hat{y}_i \) is the predicted value.

********************
Tools and Libraries
********************

Python
=========

To compute the RMSE between the actual values and predicted values, the following example can be used.

Install **scikit-learn** via this command:
:: 
   pip install -U scikit-learn
   
   
.. literalinclude:: examples/REG_RMSE/REG_RMSE.py

