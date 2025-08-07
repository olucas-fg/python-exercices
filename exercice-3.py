print("Qual é o seu sexo? (M - Masculino, F - Feminino)")
sexo = input().strip().lower()

while sexo not in ["m", "f"]:
    print("Sexo inválido! Por favor, digite 'M' para Masculino ou 'F' para Feminino.")
    sexo = input().strip().lower()

if sexo == "m":
    print("Você é homem.")
else:
    print("Você é mulher.")
