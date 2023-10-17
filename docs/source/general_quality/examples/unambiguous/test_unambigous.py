# import pandas
import pandas as pd

# load dataset
df = pd.read_csv(r"C:/Users/Datasets/marketing_campaign.csv", delimiter=";")


def find_ambiguous_sets(dataframe, list_of_columns=None):

    return dataframe[dataframe.duplicated(list_of_columns, keep="first")]
