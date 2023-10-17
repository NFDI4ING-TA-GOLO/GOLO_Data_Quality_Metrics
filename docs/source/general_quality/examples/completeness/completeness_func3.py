# import numpy
import numpy as np

def replace_missing_value(dataframe, values: list):
    """_summary_

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file
        values (list): List of values to replace with np.nan

    Returns:
        pd.dataframe: Dataframe with replaced values
    """
    for type in values:

        new_dataframe = dataframe.replace(type, np.nan)

    return new_dataframe
