while True:    
    m,n = map(int,input().split())
    c=0
    if m<=0 or n<=0:
        break
    if m<n:
        m,n = n,m
    for i in range(n,m+1,1):
        c+=i
        print(i, end=" ")
    print(f"Sum={c}")