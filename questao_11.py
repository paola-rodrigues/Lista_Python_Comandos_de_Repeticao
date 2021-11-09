"""
11º
Faça um programa que leia um número inteiro positivo N
e imprima todos os números naturais de 0 até N em ordem crescente.
"""
#Faça um programa leia número inteiro positivo
x = 0 
num = int(input('Digite um número: '))

if num > 0:
    for x in range(0, num +1):
        print(x)
        x += 1
else:
    print('Erro número Inválido')
        
        

        
        
        
