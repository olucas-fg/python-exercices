import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas as empresas e seus custos
companiesAndCost = ds[1:, [1, 6]]

# pegando apenas as missões da spacex
spacexMask = np.char.find(companiesAndCost[:, 0], "SpaceX")
spacexMissions = companiesAndCost[spacexMask >= 0]

# pegando apenas a coluna de custos e transformando em números
spacexCosts = spacexMissions[:, 1].astype(float)

# pegando a missão mais cara da spacex
mostExpensive = np.max(spacexCosts)

print(mostExpensive)
