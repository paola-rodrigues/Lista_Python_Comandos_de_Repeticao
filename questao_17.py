"""
17º
Faça um programa que leia um número inteiro positivo  N
e calcule a soma dos n primeiros números naturais.
"""
#Faça um programa leia número inteiro positivo
x = 0
soma = 0
num = int(input('Digite um número inteiro positivo: '))

if num > 0:
    for x in range(0, num +1):
        print(x)
        soma += x
    x += 1
    print(f'A soma dos números é {soma}')
else:
    print('Erro número Inválido')


