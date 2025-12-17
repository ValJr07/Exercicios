def pares():
    lista = list(map(int,input().split()))
    listaPar = []
    for i in lista:
        if i % 2 == 0:
            listaPar.append(i)
            
    for i in listaPar:
        for j in range(0, len(listaPar)-1):
            if listaPar[j] > listaPar[j+1]:
                listaPar[j], listaPar[j+1] = listaPar[j+1], listaPar[j]
                
    c=0
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista[i] = listaPar[c]
            c+=1
    
    return lista

print(pares())