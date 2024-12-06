####################################
AU-ROC (Area Under the Receiver Operating Characteristic Curve)
####################################

************
Description
************

The AU-ROC represents the capacity of the model to distinguish between a positive and a negative sample. A good model has an AUC of 1.0 and a poor model has an AUC of 0, while an AU-ROC of 0.5 means the model has no discrimination capability.
The ROC curve is created by plotting the true positive rate (TPR) against the false positive rate (FPR) at different thresholds. 

The concept of ROC and AU-ROC for multi-class classification can be described as follows:

1. **One-vs-One**: It means that for every pair of classes, a binary ROC curve is computed, and the average AU-ROC is taken. 

2. **One-vs-All**: it means that For each class, a binary ROC curve is computed considering the chosen class as positive and all other classes as negative. The AU-ROC is then averaged over all classes.


********************
Tools and Libraries
********************

To illustrate the classification metrics, the **digits** dataset provided by the **scikit-learn** library will be used. It is a dataset of hand-written digits which contains 1797 samples and each sample is an 8x8-image.
The number of classes in this dataset is 10 (corresponding to the digits from 0 to 9). This dataset will be loaded and split in `train` and test `test` (20%) sets. As a classifier, a logistic regression model will be used and trained. After the training, the model's performance will be evaluated.

Python
=========

To compute the AU-ROC for a classification problem, the following example can be used.

Install **scikit-learn** using this command:
:: 
   pip install -U scikit-learn
   
.. literalinclude:: examples/CLASS_AU_ROC/CLASS_AU_ROC.py
