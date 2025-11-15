import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose

dataset = pd.read_csv(
    "airtravel.csv", delimiter=",", index_col="Date", parse_dates=True
)

dataset["Passengers"].plot(
    figsize=(8, 6),
    title="Número de passageiros aéreos ao longo do tempo",
    xlabel="Data",
    ylabel="Número de passageiros",
    x_compat=True,
)

decomposition = seasonal_decompose(dataset["Passengers"], model="additive")
decomposition.plot()
plt.tight_layout()
plt.show()


# Análise:
# Tendência: Crescente ao longo do tempo.
# Sazonalidade: Padrões anuais visíveis, com picos entre maio e setembro.
# Ciclo: o ciclo é anual, se repete a cada ano.
