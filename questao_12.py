"""
12º
Faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem decrescente.
"""
#Faça um programa leia número inteiro positivo

num = int(input('Digite um número: '))

if num > 0:
    while(num >= 0):
        print(num)
        num -= 1
else:
    print('Erro número Inválido')
