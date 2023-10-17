def degree_of_completeness(dataframe):
    """Calculates the degree of complete entries in a dataframe

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file

    Returns:
        float: Dgree of complete entries in a give dataframe
    """

    missing_data_count = dataframe.isnull().sum().sum()

    return 1 - (missing_data_count / dataframe.size)
