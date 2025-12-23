while True:
    try:
        x = input()
        
        string = ""
        maiuscula = True
        
        for i in range(len(x)):
            if x[i].isalpha():
                if maiuscula:
                    string+=x[i].upper()
                    maiuscula = False
                else:
                    string+=x[i].lower()
                    maiuscula = True
            else:
                string+=x[i]
                
        print(string)
    except EOFError:
        break