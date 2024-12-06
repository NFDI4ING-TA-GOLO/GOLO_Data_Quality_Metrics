####################################
Precision and Recall
####################################

************
Description
************

While the Precision is the ratio of correctly predicted positive observations to the total predicted positives, Recall is the ratio of correctly predicted positive observations to all the actual positives.
These two metrics can be defined as:

.. math::
   \text{Precision} = \frac{\text{True Positives}}{\text{True Positives + False Positives}}
   
.. math::
   \text{Recall} = \frac{\text{True Positives}}{\text{True Positives + False Negatives}}


********************
Tools and Libraries
********************

To illustrate the classification metrics, the **digits** dataset provided by the **scikit-learn** library will be used. It is a dataset of hand-written digits which contains 1797 samples and each sample is an 8x8-image.
The number of classes in this dataset is 10 (corresponding to the digits from 0 to 9). This dataset will be loaded and split in `train` and test `test` (20%) sets. As a classifier, a logistic regression model will be used and trained. After the training, the model's performance will be evaluated.

Python
=========

To compute the precision and recall for a classification problem, the following example can be used.

Install **scikit-learn** using this command:
:: 
   pip install -U scikit-learn
   
.. literalinclude:: examples/CLASS_PREC_REC/CLASS_PREC_REC.py
