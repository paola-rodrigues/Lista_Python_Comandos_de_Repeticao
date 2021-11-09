"""
10º Faça um programa que calcule e mostre a soma dos 50 primeiros
números pares.
"""
x = 0
soma = 0

for x in range(0, 51):
          if x % 2 == 0:
              print(x)
              soma += x
          x += 1
print(f'soma total {soma}')          
