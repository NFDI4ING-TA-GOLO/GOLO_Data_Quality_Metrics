####################################
Consistency
####################################

*********
Description
*********
A data set must not have any contradictions within itself or with other data sets.
Data are inconsistent if different valid states are not compatible with each other.

Consistency is for measuring if two data values derived by different sets aren't conflicting with each other.
The percent of values that match across various records is a common data quality metric for consistency.

Consistency refers primarily to the use of data by different users.
Examples of consistent data usually refer to data formats and data types that should be identical throughout in order to maintain a required level of data quality.

Inconsistencies in data can be due to changes over time and/or across variables for example, in

   * Vintages or time periods
   * Units
   * Levels of accuracy
   * Levels of completeness
   * Types of inclusion or exclusions.

********************
Tools and Libraries
********************

Python
=========

Install **pandas** and **numpy** via command:
:: 
  pip install pandas

  pip install numpy

Standard deviation is absolute measure of dispersion.

.. note::
    
   Quote: However one could find which series is more consistent than other by coefficient of variation,
   that is relative measure of dispersion based on standard deviation multiplied by 100.

We can calculate consistency using standard deviation and mean of the given date:

.. note::

   Code Snipped comming soon.

The data having lower coefficient of Variation is more consistent and vice - versa.


Checking for inconsistent datatypes
-----------------------------------------

For the processing and use of data such as time series or numerical values, it is indispensable that data types must not differ. 
To check a data set for inconsistency, the following function can be used. It provides information about which columns are inconsistent.


.. literalinclude:: examples/consistency/consistency_func.py

.. code-block:: pycon

   In [1]: check_for_types(df)
           
   Out[2]: column a contains multiple different datatypes!
           

MATLAB
=========

C++
=========

********************
Literature
********************