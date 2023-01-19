entrada = int(input('Quantos termos? '))
ultimo = 0 
penultimo = 1
count = 0



if (entrada == 1):
    print(ultimo)
else:
    while count < entrada:
        print(ultimo)
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    
    
#0 - 1 - 1 - 2 - 3 - 5 - 8