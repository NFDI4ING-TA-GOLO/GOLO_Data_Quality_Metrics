********************
FAIR Metrics or Indicators
********************

Wilkonson et.al. have developed indicators that can be used by researchers to assess the FAIRness of resources such as datasets, code, workflows, and research objects. The initial survey-based FAIRness assessments utilized Gen1 and could only be assessed manually. Utilizing the survey results as a comprehensive overview of community FAIRness approaches, we subsequently developed Gen2 MIs, which are fully automated. The current iteration of the FAIR Evaluator employs Gen2 MIs.
The description of the indicators can be found in the following table

.. list-table:: The template for creating FAIR Metrics [2]
   :widths:  10 20
   :header-rows: 1

   * - FIELD, 
     - DESCRIPTION
   * - Metric Identifier
     - | FAIR Metrics should, themselves, be FAIR objects, 
       | and thus should have globally unique identifiers.
   * - Metric Name
     - A human-readable name for the metric
   * - To which principle does it apply? 
     - | Metrics should address only one subprinciple, since 
       | each FAIR principle is particular to one feature of a digital resource;
       | metrics that address multiple principles are likely to be measuring multiple features,
       and those should be separated whenever possible.
   * - What is being measured? 
     - | A precise description of the aspect of that digital
       | resource that is going to be evaluated
   * - Why should we measure it?
     - Describe why it is relevant to measure this aspect
   * - What must be provided?
     - What information is required to make this measurement?
   * - How do we measure it?
     - In what way will that information be evaluated?
   * - What is a valid result?
     - What outcome represents "success" versus "failure"
   * - For which digital resource(s) isthis relevant?
     - | If possible, a metric should apply to all digital resources;
       however, some metrics may be applicable only to a subset. 
       In this case, it is necessary to specify the range of resources
       to which the metric is reasonably applicable.
   * - Examples of their application across types of digital resource
     - Whenever possible, provide an existing example of success, and an example of failure.


Literature
=====================


.. [1] Wilkinson, M. D. et al. A design framework and exemplar metrics for FAIRness. Sci. Data 5:180118 doi: 10.1038/sdata.2018.118 (2018).
.. [2] FAIR Metrics Group. “GitHub FAIRMetrics.” (2022), [Online]. Available: https://github.com/FAIRMetrics/Metrics