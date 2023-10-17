# import numpy
import numpy as np

# define dataset
data = np.array(
    [3, 4, 4, 5, 7, 8, 12, 14, 14, 15, 17, 19, 22, 24, 24, 24, 25, 28, 28, 29]
)

# calculate standard error of the mean
np.std(data, ddof=1) / np.sqrt(np.size(data))
