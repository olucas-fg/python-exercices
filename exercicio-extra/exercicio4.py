import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando os paises e as regioes sem o cabeçaho
data = ds[1:, [0, 1]]

mascara = np.char.find(data[:, 1], "NORTHERN AMERICA")

# paises da região NORTHERN AMERICA
paisesNorthernAmerica = data[mascara != -1][:, 0]

# quantidade de paises
quantidade = np.size(paisesNorthernAmerica)
print(quantidade)
