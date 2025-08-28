import numpy as np

ds = np.loadtxt("paises.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas paises, regiao e renda
data = ds[1:, [0, 1, 8]]

# mascara para pegar apenas paises da LATIN AMER. & CARIB
mascara = np.char.find(data[:, 1], "LATIN AMER. & CARIB    ") != -1

# pegando apenas paises do LATIN AMER. & CARIB
paisesLatAm = data[mascara == True]

# pegando so a coluna de renda e transformando em numero
rendaLatAm = paisesLatAm[:, 2].astype(float)

# maior valor e posicao
maiorRenda = np.max(rendaLatAm)
posicao = np.argmax(rendaLatAm)
print(
    f"A maior renda da América Latina e Caribe é {maiorRenda} e está no país {paisesLatAm[posicao, 0]}."
)
