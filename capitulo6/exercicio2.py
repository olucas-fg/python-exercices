import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("space.csv", sep=";")

reducedDf = df[["Company Name", "Location"]]

usaEnterprises = reducedDf[reducedDf["Location"].str.contains("USA")]
usaEnterprisesWithoutRepeats = np.unique(usaEnterprises["Company Name"])
usaQuantity = len(usaEnterprisesWithoutRepeats)

chinaEnterprises = reducedDf[reducedDf["Location"].str.contains("China")]
chinaEnterprisesWithoutRepeats = np.unique(chinaEnterprises["Company Name"])
chinaQuantity = len(chinaEnterprisesWithoutRepeats)

plt.bar(
    ["USA", "China"], [usaQuantity, chinaQuantity], color=["blue", "red"], width=0.4
)
plt.show()
