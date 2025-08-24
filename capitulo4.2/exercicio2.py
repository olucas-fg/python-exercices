import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas os custos de cada missão e transformando de string para números
costColumn = ds[1:, 6].astype(float)

# pegando apenas as missões com custos disponíveis (>0)
missionsWithCost = costColumn[costColumn > 0]

# media de custos das missões espaciais
meanCost = np.mean(missionsWithCost)
print(meanCost)
