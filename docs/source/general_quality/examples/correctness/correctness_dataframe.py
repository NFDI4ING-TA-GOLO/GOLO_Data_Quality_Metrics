# import pandas
import pandas as pd
#import matplotlib
import matplotlib.pyplot as plt
#import seaborn
import seaborn as sns

# load dataset
df = pd.read_csv(r"C:/Users/Datasets/beachwater.csv", delimiter=";")

plt.figure(figsize=(16, 5))
plt.subplot(1, 1, 1)
sns.distplot(df["Water Temperature"])
plt.show()
