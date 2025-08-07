print("Quantos quilômetros terá a sua viagem?")
km = float(input("Digite a distância em km: "))

if km <= 200:
    print(f"O preço da passagem é R$ {km * 0.50:.2f}")
else:
    print(f"O preço da passagem é R$ {km * 0.45:.2f}")
