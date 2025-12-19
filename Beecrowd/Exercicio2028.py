caso=0
while True:
    try:
        num=0
        caso+=1
        n = int(input())
        l=[]
        for i in range(0,n+1):
            if i == 0:
                l.append(str(i))
                num+=1
            for j in range(i):
                l.append(str(i))
                num+=1
        
        if num == 1:
            print(f"Caso {caso}: {num} numero\n{' '.join(l)}")
            print()
        else:        
            print(f"Caso {caso}: {num} numeros\n{' '.join(l)}")    
            print()
    except EOFError:
        break