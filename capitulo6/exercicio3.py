import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("space.csv", sep=";")

reducedDf = df[["Company Name", "Status Mission"]]

roscosmosMissions = reducedDf[reducedDf["Company Name"].str.contains("Roscosmos")]

successfullMissionsOfRoscosmos = roscosmosMissions[
    roscosmosMissions["Status Mission"] == "Success"
]

qtdSuccessfullMissionsOfRoscosmos = len(successfullMissionsOfRoscosmos)
qtdFailureMissionsOfRoscosmos = (
    len(roscosmosMissions) - qtdSuccessfullMissionsOfRoscosmos
)

plt.pie(
    [qtdSuccessfullMissionsOfRoscosmos, qtdFailureMissionsOfRoscosmos],
    labels=["Success", "Failure"],
    autopct=lambda p: f"{p:.2f}%",
)
plt.show()
