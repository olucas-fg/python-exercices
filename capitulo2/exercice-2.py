print("Escolha um intervalo de números:")
inicio = int(input("Início: "))
fim = int(input("Fim: "))

print("Agora escolha um número entre eles:")
numero = int(input("Número: "))

while numero < inicio or numero > fim:
    print(f"Número inválido! Escolha entre {inicio} e {fim}.")
    print("Digite Novamente:")
    numero = int(input("Número: "))

print(f"Número válido: {numero}")
print("A tabuada de multiplicação do número escolhido:")
for i in range(01, 11):
    print(f"{numero} x {i} = {numero * i}")
