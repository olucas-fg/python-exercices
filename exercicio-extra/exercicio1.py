import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

# mostrando apenas paises,regiões, população e área dos paises
arr = ds[:, [0, 1, 2, 3]]
print(arr)
