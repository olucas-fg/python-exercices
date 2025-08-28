import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando a coluna da alfabetização sem o cabeçalho e transformando em números
alfabetizacao = ds[1:, 9].astype(float)

mediaAlfabetizacao = np.mean(alfabetizacao)
print(mediaAlfabetizacao)
