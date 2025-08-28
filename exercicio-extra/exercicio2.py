import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas as regiões
todasRegioes = ds[1:, 1]

# pegando cada região e sua quantidade
regioes, quantidade = np.unique(todasRegioes, return_counts=True)

# printando na tela
for i in range(len(regioes)):
    print(f"A região {regioes[i]} possui {quantidade[i]} países.")
