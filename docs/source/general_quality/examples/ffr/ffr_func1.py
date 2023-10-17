#import pandas
import pandas as pd

data_df = {
    "Name": ["Arpit", "Riya", "Priyanka", "Aman", "Arpit", "Rohan", "Riya", "Sakshi"],
    "Employment Type": [
        "Full-time Employee",
        "Part-time Employee",
        "Intern",
        "Intern",
        "Full-time Employee",
        "Part-time Employee",
        "Part-time Employee",
        "Full-time Employee",
    ],
    "Department": [
        "Administration",
        "Marketing",
        "Technical",
        "Marketing",
        "Administration",
        "Technical",
        "Marketing",
        "Administration",
    ],
}

df = pd.DataFrame(data_df)

# Use the DataFrame.duplicated() method to return a series of boolean values
bool_series = df.duplicated()