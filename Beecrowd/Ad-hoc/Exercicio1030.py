nc = int(input())
for i in range(nc):
    n, k = map(int,input().split())
    
    homens = [j for j in range(1,n+1) ]
    numatual = k-1

    for homem in range(len(homens)):
        if len(homens) == 1:
            print(f"Case {i+1}: {' '.join(map(str, homens))}")
            break
        
        if numatual < len(homens):    
            homens.pop(numatual)
        else:
            numatual = numatual%len(homens)
            homens.pop(numatual)

        numatual+=k-1