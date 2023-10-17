####################################
Relevance
####################################

*********
Description
*********

Relevance in data quality refers to the usefulness of collected data and whether this data is needed for further processing. 
However, the concept of "relevance" can vary depending on the specific context and requirements of your task.

In the following example, a data set is examined for a criterion, i.e. a word or a numerical value.
If the data set contains the criterion, it is classified as relevant.

********************
Tools and Libraries
********************

Install **pandas**
:: 
  pip install pandas

Python
=========

Load the needed dataset as showed in the following code snippet:

.. literalinclude:: examples/relevance/relevance_dataframe.py

If we look at the data set, we see that the first column contains the name of the individual beaches.
This is a good selection criterion to check the relevance. 

.. code-block:: pycon

   In [1]: print(df)

   Out[2]: Beach Name   Measurement Timestamp  Water Temperature  Turbidity  ... Wave Period Battery Life  Measurement Timestamp Label               Measurement ID
        0         Montrose Beach  08/30/2013 08:00:00 AM               20.3       1.18  ...         3.0          9.4            8/30/2013 8:00 AM    MontroseBeach201308300800
        1      Ohio Street Beach  05/26/2016 01:00:00 PM               14.4       1.23  ...         4.0         12.4           05/26/2016 1:00 PM  OhioStreetBeach201605261300
        2          Calumet Beach        09.03.2013 16:00               23.2       3.63  ...         6.0          9.4             09.03.2013 16:00     CalumetBeach201309031600
        3          Calumet Beach  05/28/2014 12:00:00 PM               16.2       1.26  ...         4.0         11.7           5/28/2014 12:00 PM     CalumetBeach201405281200
        4         Montrose Beach  05/28/2014 12:00:00 PM               14.4       3.36  ...         4.0         11.9           5/28/2014 12:00 PM    MontroseBeach201405281200

The following function returns whether a search word is present in the dataset. With this simple function,
the exploratory part of the data analysis can be discarded if it is clear from the beginning that relevance is not guaranteed.

.. literalinclude:: examples/relevance/relevance_func.py

With this function we can, for example, search the beach dataset for specific beaches.
In our case, we can find out if there is sensor data for Ohio Street Beach.

.. code-block:: pycon

   In [1]: df["height_new"] = df.apply(lambda row: get_inches(row["Height"]), axis=1)

   Out[2]: The dataset is relevant. It contains the keyword 'Ohio Street Beach'.

Relevance can be understood in many ways. Therefore, the previous example is only a small excerpt of what is possible.



MATLAB
=========

C++
=========

********************
Literature
********************