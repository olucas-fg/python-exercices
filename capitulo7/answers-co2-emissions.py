import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dataset = pd.read_csv(
    "co2_emissions.csv", delimiter=",", index_col="Year", parse_dates=True
)

dataset["CO2_Emissions"].plot(
    figsize=(8, 6),
    title="Emissão de CO2 ao longo do tempo",
    xlabel="Ano",
    ylabel="Emissões de CO2 (milhões de toneladas)",
    x_compat=True,
)

decomposition = seasonal_decompose(dataset["CO2_Emissions"], model="additive")
decomposition.plot()
plt.tight_layout()
plt.show()


# Análise:
# Tendência: Decrescente ao longo do tempo.
# Sazonalidade: Não ha padrão sazonal.
# Ciclo: o ciclo é a cada 8 anos aproximadamente, pois dentre esses 8 anos
# é comum a quantidade de C02 aumentar e depois diminuir.
