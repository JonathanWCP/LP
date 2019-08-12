# 10. Receba 2 números reais. Calcule e mostre a diferença desses valores.


def diferenca():
    number1 = float(input("Insira o primeiro número: "))
    number2 = float(input("Insira o segundo número: "))
    try:
        if number1 > number2:
            print("A diferença é: ", (number1 - number2))
        else:
            print("A diferença é: ", (number2 - number1))
    except ValueError:
        print("Digite um número válido!")


diferenca()
