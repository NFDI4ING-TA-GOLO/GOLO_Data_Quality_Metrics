####################################
Accuracy
####################################

************
Description
************
The overall correctness of the classifier can be determined by the accuracy. The latter is defines the ratio of the correct predictions to the total number of predections as follows: 

.. math::
   \text{Accuracy} = \frac{\text{Number of Correct Predictions}}{\text{Total Number of Predictions}}

********************
Tools and Libraries
********************

To illustrate the classification metrics, the **digits** dataset provided by the **scikit-learn** library will be used. It is a dataset of hand-written digits which contains 1797 samples and each sample is an 8x8-image.
The number of classes in this dataset is 10 (corresponding to the digits from 0 to 9). This dataset will be loaded and split in `train` and test `test` (20%) sets. As a classifier, a logistic regression model will be used and trained. After the training, the model's performance will be evaluated.

Python
=========

To compute the accuracy for a classification problem, the following example can be used.

Install **scikit-learn** using this command:
:: 
   pip install -U scikit-learn
   
.. literalinclude:: examples/CLASS_ACC/CLASS_ACC.py



MATLAB
=========

C++
=========

********************
Literature
********************