# 5. Receba os coeficientes A, B e C de uma equação do 2º grau
# (AX²+BX+C=0). Calcule e mostre as raízes reais (considerar que a
# equação possui 2 raízes).


import math


def segundoGrau():
    try:
        a = int(input("Digite o valor de A: "))
        b = int(input("Digite o valor de B: "))
        c = int(input("Digite o valor de C: "))
        delta = math.pow(b, 2) - (4*a*c)
        x1 = (-b + math.sqrt(delta)) / 2*a
        x2 = (-b - math.sqrt(delta)) / 2*a
        print(x1, x2)
    except ValueError:
        print("Digite apenas números inteiros!")


segundoGrau()
