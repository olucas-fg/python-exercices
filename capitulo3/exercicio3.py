# ler valor
print("Digite o nome do aluno:")
nome = input()
print("")
print("Digite a média do aluno:")
media = float(input())
print("")

historico = {"nome": nome, "media": media}
print(historico)
print("")

if media >= 50:
    aprovado = "AP"
else:
    aprovado = "RP"

historico["aprovado"] = aprovado

print("Novo historico")
print(historico)
