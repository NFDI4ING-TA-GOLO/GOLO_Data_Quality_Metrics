# import pandas
import pandas as pd

# load dataset
df = pd.read_csv(r"C:/Users/Datasets/marketing_campaign.csv", delimiter=";")


def find_ambiguous_sets(dataframe, list_of_columns=None):
    """

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file
        list_of_columns (list, optional): List of columns to check for duplications. Defaults to None to check every column

    Returns:
        dataframe: Dataframe with ambiguous rows to double check.
    """

    return dataframe[dataframe.duplicated(list_of_columns, keep="first")]
