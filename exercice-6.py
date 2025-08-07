import math

print("Digite um número decimal:")
numero = float(input())

print("Raiz quadrada: ", numero**0.5)
print("Arredondando para baixo: ", math.floor(numero))
print("Arredondando para cima: ", math.ceil(numero))
print("Parte inteira: ", math.trunc(numero))
