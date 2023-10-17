####################################
Uniformity
####################################

*********
Description
*********

The information of a data set must be structured in a uniform way.
Data of the same type should also have the same dimensions.

Uniformity is therefore specific to metrics and units of measurement, and is particularly important when data comes from different sources.

In the following examples, data will be compared for uniformity and if necessary recalculated to fit uniformity.

********************
Tools and Libraries
********************

Install **pandas**
:: 
  pip install pandas

Python
=========

Load the needed dataset as showed in the following code snippet:

.. literalinclude:: examples/uniformity/uniformity_func1.py

.. code-block:: pycon

   In [1]: print(df.head())
           
   Out[2]:       Name  Height Handedness
          0      Jon    6'5"      Right
          1      Rob  6'7.5"       Left
          2   Sharon    6'3"      Right
          3     Alex    6'2"      Right
          4  Rebecca      7'      Right

As you can see, the height column contains impirical dimensions. For further processing or comparison with metric data,
it is necessary to convert from feet and inches to metres and centimetres.

The following function can be used to convert the data from inches to metres.

.. literalinclude:: examples/uniformity/count_inches.py

Now you can apply this function to the whole column and recalculate to meters

.. code-block:: pycon

   In [1]: df["height_new"] = df.apply(lambda row: get_inches(row["Height"]), axis=1)

   Out[2]:       Name  Height Handedness  height_new
          0      Jon    6'5"      Right      195.58
          1      Rob  6'7.5"       Left      201.93
          2   Sharon    6'3"      Right      190.50
          3     Alex    6'2"      Right      187.96
          4  Rebecca      7'      Right      213.36
          5   Ariane    5'8"       Left      172.72
          6    Bryon      7'      Right      213.36
          7    Brett      6'      Right      182.88
          8     Matt    5'5"      Right      165.10

After applying the function, all body sizes were converted from imperial system to metric system.

MATLAB
=========

C++ 
=========

********************
Literature
********************