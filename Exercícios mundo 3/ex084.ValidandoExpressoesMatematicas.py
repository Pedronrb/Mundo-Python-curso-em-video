expr = str(input('Digite uma expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Sua expressão é válida!!')
else:
    print('Sua expressão está errada!!')

'''

listas = []
aberto = 0
fechado = 0
exp = str(input(''))
for simb in exp:
    if simb == '(':
        aberto += 1
    elif simb == ')':
        fechado += 1 
if aberto == fechado:
    print('Válido')
else:
    print('Inválido')   '''     