import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("2019.csv")

data = df["Economy (GDP per Capita)"]
print(data)


#plt.bar([1,2,3,4,5], data)
#plt.show()