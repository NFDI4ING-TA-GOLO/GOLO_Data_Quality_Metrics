####################################
R-Squared (R²)
####################################

************
Description
************

Known as the coefficient of determination, R² identifies how well the predictions performed by the model fit (match) the acutual data. On a scale of 0 to 1, the strength of the relationship between the model and the actual data will be measured. However, it does not tell you whether your model is correct or meaningful.
The R² is defined as:

.. math::
   \text{R²} = 1 - \frac{\sum_{i=1}^{n} (y_i - \hat{y}_i)^2}{\sum_{i=1}^{n} (y_i - \bar{y})^2}

where:

- \( n \) is the number of observations.
- \( y_i \) is the actual value.
- \( \hat{y}_i \) is the predicted value.
- \( \bar{y} \) is the mean of the actual values.

********************
Tools and Libraries
********************

Python
=========

To compute the R² between the actual values and predicted values, the following example can be used.

Install **scikit-learn** via this command:
:: 
   pip install -U scikit-learn
   
   
.. literalinclude:: examples/REG_R_Squared/REG_R_Squared.py


MATLAB
=========

C++
=========

********************
Literature
********************