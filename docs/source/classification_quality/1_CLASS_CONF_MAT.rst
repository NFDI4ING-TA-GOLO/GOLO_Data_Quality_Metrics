####################################
Confusion Matrix
####################################

************
Description
************

Confusion Matrix
================
The confusion matrix, described as an nxn-Matrix, where n the number of the classes is used for measuring the performance of a classification model. 

For a binary classification problem, the confusion matrix is a 2x2 Matrix defined as follows:

- **TP (True Positive)**: Both the actual class and the predicted class are positive.
- **TN (True Negative)**: Both the actual class and the predicted class are negative.
- **FP (False Positive)**: The actual class is negative but the predicted class is positive.
- **FN (False Negative)**: The actual class is positive but the predicted class is negative.

For multi-class classification with N classes, the confusion matrix is an NxN matrix. Each class is treated as the "positive" class in turn, while all other classes are treated as "negative".

For example, computing the TP, TN, FP and FN for the digit "4" can be accomplished as follows:

- **True Positives (TP) for 4**: The number of actual "4"s correctly predicted as "4".
- **True Negatives (TN) for 4**: The number of samples that are not "4" and are also not predicted as "4".
- **False Positives (FP) for 4**: The number of samples that are not "4" but are incorrectly predicted as "4".
- **False Negatives (FN) for 4**: The number of actual "4"s incorrectly predicted as some class other than "4".


********************
Tools and Libraries
********************

To illustrate the classification metrics, the **digits** dataset provided by the **scikit-learn** library will be used. It is a dataset of hand-written digits which contains 1797 samples and each sample is an 8x8-image.
The number of classes in this dataset is 10 (corresponding to the digits from 0 to 9). This dataset will be loaded and split in `train` and test `test` (20%) sets. As a classifier, a logistic regression model will be used and trained. After the training, the model's performance will be evaluated.

Python
=========

To compute the confusion matrix for a classification problem, the following example can be used.

Install **scikit-learn** using this command:
:: 
   pip install -U scikit-learn
   
.. literalinclude:: examples/CLASS_CONF_MAT/CLASS_CONF_MAT.py

.. code-block:: pycon
    [[27  0  0  0  0  0  0  0  0  0]
    [ 0 31  0  0  0  0  1  0  2  1]
    [ 0  0 35  1  0  0  0  0  0  0]
    [ 0  0  0 29  0  0  0  0  0  0]
    [ 0  0  0  0 30  0  0  0  0  0]
    [ 0  0  0  0  0 37  0  0  0  3]
    [ 0  1  0  0  0  0 43  0  0  0]
    [ 0  0  0  0  1  0  0 38  0  0]
    [ 0  2  1  0  0  0  0  0 36  0]
    [ 0  0  0  0  0  1  0  0  1 39]]
