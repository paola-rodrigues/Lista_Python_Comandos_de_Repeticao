"""
7º Faça um programa que leia 10 inteiros positivos, ignorando não positivos, 
e imprima sua média.
"""

cont = 1
soma = 0
    
while cont <= 10:
    num = int(input(f'Digite {cont}º positivo: '))
    if num > 0:
        cont += 1
        soma += num
    else:
        print('Erro Número Inválido')
    
print(f'A média dos números inteiros positivos é {soma/(cont -1)}')

    

    
