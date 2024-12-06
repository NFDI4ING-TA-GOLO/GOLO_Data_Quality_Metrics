.. _General quality metrics:

####################################
General quality metrics
####################################

Data, regardless of location of recording, temporal dimension, level of pre-processing or type of collection, are subject to certain quality metrics.
These metrics are used to assess how useful or relevant large data sets or collected data are. 

Data sets can be reliably described using the following metrics.

   * `Completeness <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id7>`_
   * `Unambiguous <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id12>`_
   * `Correctness <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id19>`_
   * `Timeliness <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#timeliness-and-punctuality>`_
   * `Accuracy <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id32>`_ 
   * `Consistency <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id39>`_
   * `freedom_from_redundancy <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id46>`_
   * `Relevance <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id53>`_ 
   * `Uniformity <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id60>`_
   * `Reliability <https://quality.nfdi4ing.de/en/latest/general_quality/general_quality.html#id67>`_ 
   
Of these eleven criteria, all are used in the rarest cases. Which criteria 
are used depends on the data set and the purpose of the data.
Experience shows that the first six criteria are used for data analysis.

******************
Datasets
******************

To test the individual quality metrics, the internet provides free data sets. These data sets can be downloaded from the following link.
The programming and analysis examples should largely refer to these data.

`Datasciene Datasets <https://towardsdatascience.com/all-the-datasets-you-need-to-practice-data-science-skills-and-make-a-great-portfolio-74f2eb53b38a>`_

In order to test one's datascience skills on simple and practical datasets, the author of the blog towardsdatascience.com provides over 50 datasets.
These can then be integrated into your own IDE or downloaded via the Github page.

`Machine Learning Datasets <https://www.kaggle.com/datasets>`_

Kaggle provides more than 50,000 data sets. This data can be used, for example, as the basis for machine learning algorithms.
For this purpose, however, it is necessary to check the data beforehand and to change it if necessary.

`Scientific Data <https://www.nature.com/collections/ebaiehhfhg>`_

Nature.com sources data sets from around the world that relate largely to the Corona pandemic.


********************
Tools and Libraries
********************


Python
=========

`YData <https://github.com/ydataai>`_

ydata_quality is an open-source python library for assessing Data Quality throughout the multiple stages of a data pipeline development.

*A holistic view of the data can only be captured through a look at data from multiple dimensions and ydata_quality evaluates it in a modular way wrapped into a single Data Quality engine.
This repository contains the core python source scripts and walkthrough tutorials.*

`Pandas <https://pandas.pydata.org/>`_

*Pandas is a fast, powerful, flexible and easy to use open source data analysis and manipulation tool,
built on top of the Python programming language.*

`NumPy <https://numpy.org/>`_

*NumPy offers comprehensive mathematical functions, random number generators, linear algebra routines, Fourier transforms, and more.*

********************
Literature
********************

.. [1] Batini, C., & Scannapieco, M. (2006). Data Quality: Concepts, Methodologies and Techniques. Springer.
.. [2] Smith, J. (2016). Title of the Paper. Proceedings of the Conference, 10-15. Retrieved from `https://ceur-ws.org/Vol-1753/paper5.pdf`
.. [3] Johnson, A., & Smith, B. (2014). Title of the Paper. In Proceedings of the Conference (pp. 100-110). Retrieved from `https://ieeexplore.ieee.org/document/6816764`
.. [4] Torchiano, M., & Vetro', A. (2015). Title of the Paper. Journal of Open Data Quality, 3(1). Retrieved from `https://nexacenter.org/nexacenterfiles/torchiano-vetro-odq2015.pdf`
.. [5] Business Information Excellence. Retrieved from `https://www.business-information-excellence.de/datenqualitaet/86-datenqualitaet-messen-11-datenqualitaets-kriterien`

.. include:: 0_Completeness.rst
.. include:: 01_Unambiguous.rst
.. include:: 02_Correctness.rst
.. include:: 03_Timeliness.rst 
.. include:: 04_Accuracy.rst 
.. include:: 05_Consistency.rst 
.. include:: 06_freedom_from_redundancy.rst
.. include:: 07_Relevance.rst 
.. include:: 08_Uniformity.rst 
.. include:: 09_Reliability.rst 