"""
15º
Faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números ímpares de 0 até N em ordem crescente.
"""
#Faça um programa leia número inteiro positivo
cont = 0
num = int(input('Digite um número positivo ímpar: '))

if num > 0 and num % 2 == 1:
    for cont in range(0, num +1):
        if cont % 2 == 1:
            print(cont)
    cont += 1
else:
    print('Erro número Inválido')
