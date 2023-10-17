# import pandas
import pandas as pd

# import numpy
import numpy as np

# dictionary of lists
dict = {
    "column a": [0, 90, np.nan, 95],
    "column b": [30, 45, 56, 0],
    "column c": [np.nan, 40, 80, 98],
    "column d": [np.nan, 12, 35, None],
}

# creating a dataframe from list
df = pd.DataFrame(dict)
