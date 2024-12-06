####################################
F1-score
####################################

************
Description
************

The F1-score is a combination of the precision and recall, which is defined by calculating the harmonic mean of the two metrics. Its mathematical equation is described as follows:

.. math::
   \text{F1-score} = 2 \times \frac{\text{Precision} \times \text{Recall}}{\text{Precision} + \text{Recall}}

********************
Tools and Libraries
********************

To illustrate the classification metrics, the **digits** dataset provided by the **scikit-learn** library will be used. It is a dataset of hand-written digits which contains 1797 samples and each sample is an 8x8-image.
The number of classes in this dataset is 10 (corresponding to the digits from 0 to 9). This dataset will be loaded and split in `train` and test `test` (20%) sets. As a classifier, a logistic regression model will be used and trained. After the training, the model's performance will be evaluated.

Python
=========

To compute the F1-score for a classification problem, the following example can be used.

Install **scikit-learn** using this command:
:: 
   pip install -U scikit-learn
   
.. literalinclude:: examples/CLASS_F1_SCORE/CLASS_F1_SCORE.py
