import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("paises.csv", sep=";")
reducedDf = df[["Country", "Region", "Deathrate", "Birthrate"]]
print(reducedDf)

northAmericaDf = reducedDf[reducedDf["Region"] == "NORTHERN AMERICA                   "]

x = northAmericaDf["Country"].values
y1 = northAmericaDf["Birthrate"].values
y2 = northAmericaDf["Deathrate"].values

plt.xlabel("Países")
plt.ylabel("Taxas")

plt.plot(x, y1, "o:g")
plt.plot(x, y2, "o:b")
plt.show()
