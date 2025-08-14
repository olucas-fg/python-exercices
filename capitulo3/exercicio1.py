# lista em python
topBrasileirao = ["Flamengo", "Cruzeiro", "Palmeiras", "Bahia", "Botafogo", "Barcelona"]

print(topBrasileirao[0:3])
print(topBrasileirao[3:5])
print(sorted(topBrasileirao))

# imprimir a posição
if "Barcelona" in topBrasileirao:
    posicao = topBrasileirao.index("Barcelona") + 1
    print("Barcelona está na posição:", posicao)
else:
    print("Barcelona não está na lista.")
