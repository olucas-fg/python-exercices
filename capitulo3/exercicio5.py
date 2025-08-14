pessoas = []

print("Quantas pessoas participarão do teste?")
qtd_pessoas = int(input())

for i in range(qtd_pessoas):
    print("Qual o nome da pessoa?")
    nome = input()
    print("")
    print("Qual a idade da pessoa?")
    idade = int(input())
    print("")
    print("Qual o sexo da pessoa?")
    sexo = input()
    print("")
    pessoas.append({"nome": nome, "idade": idade, "sexo": sexo})

print(pessoas)
print("")

# media de idade do grupo
soma_idade = 0
for p in pessoas:
    soma_idade += p["idade"]
media_idade = soma_idade / len(pessoas)
print("A média de idade do grupo é:", media_idade)

# mulheres que tem menos de 20 anos
soma_mulheres_menos_20 = 0
for m in pessoas:
    if m["sexo"].lower() == "f" and m["idade"] < 20:
        soma_mulheres_menos_20 += 1
print("Mulheres com menos de 20 anos:", soma_mulheres_menos_20)
