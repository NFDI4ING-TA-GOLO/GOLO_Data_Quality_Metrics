def complete_data_series(dataframe):
    """Calcualtes the degree of complete rowwise entries in a give dataframe

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file

    Returns:
        float: Degree of complete rowwise entries in a give dataframe

    """

    row_count_missing_data = dataframe.isnull().any(axis=1).sum()

    return 1 - (row_count_missing_data / len(dataframe))
