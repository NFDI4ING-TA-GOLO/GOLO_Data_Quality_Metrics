def degree_of_unambiguous(dataframe, list_of_columns=None):
    """Sums up numbwe of ambiguous rows

    Args:
        dataframe (pd.dataframe): Input dataframe created from a csv-file

    Returns:
        float: Degree of which a dataframe is unambiguous
    """

    sum_of_duplicates = dataframe.duplicated(subset=list_of_columns, keep="first").sum()

    return ((dataframe.size - sum_of_duplicates) / dataframe.size) * 100
