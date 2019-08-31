# 9. Receba os 2 números inteiros. Calcule e mostre a soma dos quadrados.


import math


def quadrado():
    try:
        a = int(input("Digite o primeiro número inteiro: "))
        b = int(input("Digite o segundo número inteiro: "))
        a = math.pow(a, 2)
        b = math.pow(b, 2)
        print("Primeiro número: ", a)
        print("Segundo número: ", b)
    except ValueError:
        print("Digite apenas números inteiros!")


quadrado()
