# 4. Receba a temperatura em graus Celsius. Calcule e mostre a sua
# temperatura convertida em fahrenheit F = (9*C+160) /5.


def fahrenheit():
    try:
        c = int(input("Digite a temperatura em graus Celsius: "))
        f = (9*c+160)/5
        print("Resultado: ", f)
    except ValueError:
        print("Digite apenas números inteiros!")


fahrenheit()
