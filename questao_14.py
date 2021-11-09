"""
14º
Faça um programa que leia um número inteiro positivo par N
e imprima todos os números pares de 0 até N em ordem decrescente.
"""
#Faça um programa leia número inteiro positivo
cont = 0
num = int(input('Digite um número inteiro positivo par: '))

if num > 0 and num % 2 == 0:
    while(num >= 0):
        if num % 2 == 0:
            print(num)
        num -= 1
else:
    print('Erro número Inválido')
