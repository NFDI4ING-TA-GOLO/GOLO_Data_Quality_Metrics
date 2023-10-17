def count_missing_value(dataframe):
    """Counts missing values in a dataframe

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file

    Returns:
        int: Summed up counts of missing values
    """

    return dataframe.isnull().sum()
