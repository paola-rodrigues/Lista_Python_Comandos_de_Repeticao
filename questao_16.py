"""
16º
Faça um programa que leia um número inteiro positivo ímpar N
e imprima todos os números ímapres de 0 até N em ordem decrescente.
"""
#Faça um programa leia número inteiro positivo
cont = 0
num = int(input('Digite um número inteiro positivo ímpar: '))

if (num > 0) and (num % 2 == 1):
    while(num >= 0):
        if num % 2 == 1:
            print(num)
        num -= 1
else:
    print('Erro número Inválido')

