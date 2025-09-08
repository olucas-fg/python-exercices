import pandas as pd

# Questão 1
seriesAno1 = pd.Series({"Java": 16.25, "C": 16.04, "Python": 9.85})
seriesAno2 = pd.Series({"C": 16.21, "Python": 12.12, "Java": 11.68})

# Questão 2
# Total ano 1:
totalAno1 = seriesAno1.sum()
print(totalAno1)
# Total ano 2:
totalAno2 = seriesAno2.sum()
print(totalAno2)

# Questão 3
crescimentoOuDeclinio = ((seriesAno2 / seriesAno1) * 100) - 100
print(crescimentoOuDeclinio)

# Questão 4
apenasQueCresceram = crescimentoOuDeclinio[crescimentoOuDeclinio > 1]
print(apenasQueCresceram)

# Questão 5
taxa = (crescimentoOuDeclinio / 100) + 1
print(taxa)
previsaoAno4 = seriesAno2 * (taxa**2)
maisPopular = previsaoAno4.nlargest(1)
print(maisPopular)
