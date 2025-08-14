# dois conjuntos
loja1 = {"iphone11", "iphone12", "iphone13", "iphone14"}
loja2 = {"iphone12", "iphone13", "iphone14", "galaxyS23", "galaxyS24"}

# modelos disponíveis
print("Modelos disponíveis na loja 1: ")
print(loja1)
print("")
print("Modelos disponíveis na loja 2: ")
print(loja2)
print("")


# todos os possíveis modelos de serem comprados nas duas lojas
print("Modelos disponíveis nas duas lojas: ")
print(loja1 | loja2)
