# import re
import re

import pandas as pd

r = re.compile(r"(?:^(?:(\d+)')?(?:[-| ]*)(?:(\d*(?: ?\d+\/\d+)?|(?:\d*\.\d+)?)?\")?$)")

def get_inches(height):
    """Calculates the number of inches in a given impirical height.

    Args:
        height (string): hieght consisting of feet and inches as string

    Returns:
        float: Number of inches
    """
    m = r.match(height)

    print(int(m.group(1)))

    if not m.groups()[1]:
    
        return float('NaN') if m is None else int(m.group(1))*30.48
    
    else:

        return float('NaN') if m is None else float(m.group(1))*30.48 + float(m.group(2))*2.54


# load dataset
df = pd.read_csv(r"C:\Users\Datasets\basketballteam.csv", delimiter=",")

df["height_new"] = df.apply(lambda row: get_inches(row["Height"]), axis=1)

print(df)