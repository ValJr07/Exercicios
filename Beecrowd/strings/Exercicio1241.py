n = int(input())

for i in range(n):
    a,b = map(str, input().split())
    
    if len(b) > len(a):
        a,b = b,a
    
    indicefinal = len(a) - len(b)
    
    if a[indicefinal:len(a)] == b:
        print("encaixa")
    else:
        print("nao encaixa")