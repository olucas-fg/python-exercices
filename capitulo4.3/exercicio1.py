import numpy as np

ds = np.loadtxt("space.csv", delimiter=";", dtype=str, encoding="utf-8")

# pegando apenas "success" ou "failure"
statusMission = ds[1:, 7]

# máscara de true ou false
successMask = np.char.startswith(statusMission, "Success")

# pegando apenas missões bem-sucedidas
successMissions = statusMission[successMask]

# pegando a quantidade total e a quantidade de missões bem-sucedidas
totalMissions = len(statusMission)
successMissionsQuantity = len(successMissions)

percentageOfSuccess = (successMissionsQuantity / totalMissions) * 100
print(percentageOfSuccess)
