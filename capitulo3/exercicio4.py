pessoas = {}

for i in range(3):
    print(f"Digite o nome da pessoa {i}:")
    nome = input()
    print("")
    print(f"Digite o peso da pessoa {i}:")
    peso = float(input())
    print("")

    pessoas[f"pessoa{i}"] = {"nome": nome, "peso": peso}

print("Todas as pessoas:")
print(pessoas)
print("")

# pessoa mais pesada e mais leve
print("Pessoa mais pesada: ")
pessoa_mais_pesada = max(pessoas, key=lambda x: pessoas[x]["peso"])
print(pessoas[pessoa_mais_pesada]["nome"])
print("")

print("Pessoa mais leve: ")
pessoa_mais_pesada = min(pessoas, key=lambda x: pessoas[x]["peso"])
print(pessoas[pessoa_mais_pesada]["nome"])
