"""
8º Escreva um programa que leia 10 números e escreva o menor valor lido
e o maior valor lido.
"""
cont = 1

lista = []    
while cont <= 10:
    num = int(input(f'Digite {cont}º positivo: '))
    lista.append(num)
    cont += 1

menor = min(lista)
maior = max(lista)
    
print(f'O menor valor digítado foi {menor}')
print(f'O maior valor digítado foi {maior}')
