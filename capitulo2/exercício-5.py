print("Digite um número entre 1000 e 9999:")
numero = int(input())

while numero < 1000 or numero > 9999:
    print("Número inválido! Por favor, digite um número entre 1000 e 9999:")
    numero = int(input())

print("Número válido!!")
print("Número da unidade: ", numero // 1 % 10)
print("Número da dezena: ", numero // 10 % 10)
print("Número da centena: ", numero // 100 % 10)
print("Número do milhar: ", numero // 1000 % 10)
