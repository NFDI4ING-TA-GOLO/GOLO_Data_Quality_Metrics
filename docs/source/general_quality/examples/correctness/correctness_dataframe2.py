# import pandas
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
#import seaborn
import seaborn as sns

# load dataset
df = pd.read_csv(r"C:/Users/Datasets/beachwater.csv", delimiter=";")


df[(df["Water Temperature"] > 29.43) | (df["Water Temperature"] < 9.29)]

new_df = df[(df["Water Temperature"] < 29.43) & (df["Water Temperature"] > 9.29)]


plt.figure(figsize=(16, 5))
plt.subplot(1, 1, 1)
sns.distplot(new_df["Water Temperature"])
plt.show()
