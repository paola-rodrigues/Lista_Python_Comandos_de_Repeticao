"""
1º Faça um programa que determine o mostre os cinco primeiros múltiplos de 3,
considerando números maiores que 0.
"""
cont = 1
num = 0
while num < 5:
    if cont % 3 == 0:
        print(cont)
        num += 1
    cont += 1
    
