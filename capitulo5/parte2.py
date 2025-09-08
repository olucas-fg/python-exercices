import pandas as pd
import numpy as np

# questão 6
np.random.seed(10)
df = pd.DataFrame(
    index=["A", "B", "C", "D", "E"],
    columns=["W", "X", "Y", "Z"],
    data=np.random.randint(1, 50, size=(5, 4)),
)
print(df)

columnX = df["X"]
xMenorQue30 = columnX[columnX < 30]
MediaXMenorQue30 = xMenorQue30.mean()
print(MediaXMenorQue30)

# Questão 7
linhaD = df.loc["D"]
mediaLinhaD = linhaD.mean()
print(mediaLinhaD)

linhaE = df.iloc[4]
somaLinhaE = linhaE.sum()
print(somaLinhaE)

# Questão 8
slicing = df.loc[["A", "C", "E"], ["X", "Y"]]
print(slicing)
somaLinhas = np.sum(slicing.values, axis=1)
print(somaLinhas)
somaColunas = np.sum(slicing.values, axis=0)
print(somaColunas)
