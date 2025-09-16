import numpy as np
import pandas as pd

df = pd.read_csv("paises.csv", delimiter=";")

# Questão 1 a
countriesPerRegion = df.groupby("Region").sum()["Country"]
oceanicCountries = countriesPerRegion["OCEANIA                            "]
print("Questão 1a:")
print(oceanicCountries)
print("--------------------------------------------------")

# Questão 1 b
qtdCountriesPerRegion = df.groupby("Region").count()["Country"]
qtdOceanicCountries = qtdCountriesPerRegion["OCEANIA                            "]
print("Questão 1b:")
print(qtdOceanicCountries)
print("--------------------------------------------------")

# Questão 2
# nome, região e população
df2 = df[["Country", "Region", "Population"]]
countryAndRegionWithMaxPopulation = df2[df2["Population"] == df2["Population"].max()]
print("Questão 2:")
print(countryAndRegionWithMaxPopulation.iloc[0, 0:2])
print("--------------------------------------------------")

# Questão 3
meanLiteracyPerRegion = df.groupby("Region")["Literacy (%)"].mean()
print("Questão 3:")
print(meanLiteracyPerRegion)
print("--------------------------------------------------")

# Questão 4
countriesAndCost = df[["Country", "Coastline (coast/area ratio)"]]
mask = countriesAndCost["Coastline (coast/area ratio)"] == 0
noCostCountries = countriesAndCost[mask]["Country"]
print("Questão 4:")
noCostCountries.to_csv("noCoast.csv", sep=";")
print("--------------------------------------------------")


# Questão 5
def mortalityRate(value):
    if value < 9:
        return "Balanced"
    return "Urgent"


mortalityRates = df["Deathrate"]
humanitarianHelp = mortalityRates.apply(mortalityRate)
df["Humanitarian Help"] = humanitarianHelp

print("Questão 5:")
print(df)
print("--------------------------------------------------")
