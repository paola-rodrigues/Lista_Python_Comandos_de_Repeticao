"""
5º Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
cont = 1
soma = 0

for cont in range(1,11):
    valor = int(input(f'Digite {cont}º valor: '))
    soma += valor
    cont += 1
print(f'A soma dos {cont-1} valores é {soma}')            
