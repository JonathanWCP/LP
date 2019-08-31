# 11. Receba o raio de uma circunferência. Calcule e mostre o comprimento da
# circunferência.


import math


def comprimento():
    try:
        raio = int(input("Digite o raio da circunferência: "))
        comp = 2 * math.pi * raio
        print("O Comprimento da circunferência é de ", comp)
    except ValueError:
        print("Digite apenas números inteiros!")


comprimento()
