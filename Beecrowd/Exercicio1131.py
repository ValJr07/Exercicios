c=0; ci=0; cg=0; emp=0; 
while True:    
    i,g = map(int,input().split())
    if i>g:
        ci+=1
    elif g>i:
        cg+=1
    else:
        emp+=1
    c+=1
    print("Novo grenal (1-sim 2-nao)")
    x=int(input())
    if x==2:
        break
if ci>cg:
    x1 = "Inter venceu mais"
elif cg>ci:
    x1 = "Gremio venceu mais"
else:
    x1 = "Não houve vencedor"
print(f"{c} grenais\nInter:{ci}\nGremio:{cg}\nEmpate:{emp}\n{x1}")