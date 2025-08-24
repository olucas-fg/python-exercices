import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas as localidades de cada missão
missionsLocation = ds[1:, 2]

# encontrando as missões feitas apenas pelos estados unidos
usaMask = np.char.find(missionsLocation, "USA")

# quantidade de missões feitas pelos estados unidos
usaMissionsQuantity = usaMask[usaMask >= 0].size

print(usaMissionsQuantity)
