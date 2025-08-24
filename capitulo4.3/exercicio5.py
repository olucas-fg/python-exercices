import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando os nomes das empresas que realizaram missões
comapanies = ds[1:, 1]

# pegando cada empresa e a quantidade de vezes que ela aparece
uniqueCompanies, counts = np.unique(comapanies, return_counts=True)

# mostrando quantas vezes cada empresa realizou missões
for i in range(len(uniqueCompanies)):
    print(f"A empresa {uniqueCompanies[i]} realizou {counts[i]} missões.")
