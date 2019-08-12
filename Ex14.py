# 14. Receba 2 ângulos de um triângulo. Calcule e mostre o valor do 3º ângulo.


def triangulo():
    try:
        angulo1 = int(input("Digite o valor do primeiro ângulo: "))
        angulo2 = int(input("Digite o valor do segundo ângulo: "))
        triangle = 180 - (angulo1 + angulo2)
        print("O valor do terceiro ângulo é de", triangle)
    except ValueError:
        print("Digite apenas valores inteiros!")


triangulo()
