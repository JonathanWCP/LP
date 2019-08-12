# 3. Receba a base e a altura de um triângulo. Calcule e mostre a sua área.


def calculaAreaT():
    try:
        b = int(input("Digite a base do triângulo: "))
        h = int(input("Digite a altura do triângulo: "))
        result = (b*h)/2
        print("Resultado: ", result)
    except ValueError:
        print("Digite apenas valores inteiros!")

calculaAreaT()
