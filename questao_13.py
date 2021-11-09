"""
13º
Faça um programa que leia um número inteiro positivo N
e imprima todos os números pares de 0 até N em ordem crescente.
"""
#Faça um programa leia número inteiro positivo
cont = 0
num = int(input('Digite um número: '))

if num > 0:
    for cont in range(0, num +1):
        if cont % 2 == 0:
            print(cont)
    cont += 1
else:
    print('Erro número Inválido')
