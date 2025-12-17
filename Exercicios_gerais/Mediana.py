import math

num1 = list(map(int,input().split()))
num2 = list(map(int,input().split()))

lista_inteira = num1 + num2

for i in lista_inteira:
    for j in range(0, len(lista_inteira)-1):
        if lista_inteira[j]> lista_inteira[j+1]:
            lista_inteira[j], lista_inteira[j+1] = lista_inteira[j+1], lista_inteira[j]
            
def mediana():
    if len(lista_inteira) % 2 != 0:
        medianaLista = lista_inteira[math.floor(len(lista_inteira)/2)]
    else:
        NumMaior = lista_inteira[int(len(lista_inteira)/2)]
        NumMenor = lista_inteira[int(len(lista_inteira)/2-1)]
        medianaLista = (NumMaior+NumMenor)/2
    return medianaLista

print(f"Lista Ordenada: {lista_inteira}\nMediana: {mediana()}")        