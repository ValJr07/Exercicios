while True:
    try:
        linhas, colunas = map(int,input().split())
        
        campo = []
        for i in range(linhas):
            valores = list(map(int,input().split()))
            campo.append(valores)
            
            for j in range(colunas):
                if campo[i][j] == 1:
                    localjogador = (i,j)
                    ji = i
                    jj = j
                elif campo[i][j] == 2:
                    localpokemon = (i,j)
                    pi = i
                    pj = j
                
        print(abs(ji - pi) + abs(jj - pj))
    except EOFError:
        break