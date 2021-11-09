"""
9º Faça um programa que leia um número inteiro N e depois imprima
os N primeiros números naturais ímapres.
"""

x = 0
#1 primeiro passo leia número inteiro N

num = int(input('Digite um número inteiro: '))

# 2 passo imprima os n primeiros números naturais impares

for x in range(0, num + 1):
          if x % 2 == 1:
              print(x)
          x += 1
          
          
          
    
          
