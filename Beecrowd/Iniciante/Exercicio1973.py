n = int(input())
x = list(map(int,input().split()))
c=0

if len(x) == n:
    for i in range(0, len(x)):
        if x[i] % 2 == 0:
            x[i]-=1
            c+=1
            for j in range(i-1,-1,-1):
                if x[j] == 0:
                    continue
                x[j] = x[j]-1
            break
        else:
            try:
                c+=1
                x[i] = x[i]-1
            except IndexError:
                break
    print(c,sum(x))