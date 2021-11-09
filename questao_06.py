"""
6 º Faça um programa que leia 10 inteiros e imprima sua média.
"""
cont = 1
soma = 0

for cont in range(1,11):
    valor = int(input(f"Digite {cont} valor: "))
    soma += valor
    cont += 1
print(f'A média dos valores foi {soma/(cont -1)}')            
