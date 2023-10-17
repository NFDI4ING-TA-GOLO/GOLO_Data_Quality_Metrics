####################################
Unambiguous
####################################

*********
Description
*********
Each data record must be unambiguously interpretable.
If entries differ only by one characteristic or only by the ID, a duplicate analysis
is to be preferred because there is reasonable doubt that it is not the same entry.

********************
Tools and Libraries
********************

Python
=========

In Python’s Pandas library, Dataframe class provides a member function to find duplicate rows based on all columns or some specific columns.
It returns a Boolean Series with True value for each duplicated row.

Find ambiguous entries
----------------------

To check if rows occur multiple time you can use this code snippet which will check if an row is identical to a provious row.

.. literalinclude:: examples/unambiguous/unambiguous_func1.py

If used on the preloaded dataframe the function shows that three rows are duplicates. With the list_of_columns-Parameter
you can subset the columns to find duplicated column values. The more values there are that more ambiguous a dateset can be.

.. code-block:: pycon

   In [1]:  find_ambiguous_sets(dataframe, list_of_columns=None)

   Out[2]:  ID  Year_Birth   Education Marital_Status   Income  ...  AcceptedCmp2  Complain Z_CostContact  Z_Revenue  Response
            89   3033        1963      Master       Together  38620.0  ...             0         0             3         11         0
            131  4646        1951    2n Cycle        Married  78497.0  ...             0         0             3         11         0
            197   326        1973  Graduation        Married  51148.0  ...             0         0             3         11         0

Measure unambiguous
----------------------

Since the pure number of duplicated columns has little significance, the following function can be used to determine the degree of uniqueness.
Since only three entries are duplicated, the degree is almost one.

.. literalinclude:: examples/unambiguous/unambiguous_func2.py


.. code-block:: pycon

   In [1]:  degree_of_unambiguous(df)

   Out[2]:  99.86625055728935




MATLAB
=========

C++
=========

********************
Literature
********************