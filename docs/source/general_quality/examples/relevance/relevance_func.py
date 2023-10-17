def check_dataset_relevance(df, keyword):
    """This function gives feedback if a given keywords exists in a dataframe.

    Args:
        df (dataframe): dataframe to search in
        keyword (string): Keyword as criteria to look for in the given dataframe
    """
       
    # Check if the keyword is present in any column of the DataFrame
    keyword_found = any(df.apply(lambda row: keyword in str(row), axis=1))
    
    if keyword_found:
        print(f"The dataset is relevant. It contains the keyword '{keyword}'.")
    else:
        print(f"The dataset is not relevant. It does not contain the keyword '{keyword}'.")