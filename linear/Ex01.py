# 1. Coletar o valor do lado de um quadrado, calcular sua área e apresentar o resultado.
def ladoquadrado():
    try:
        print("Calculo de área do quadrado")
        print("Digite o valor do lado de um quadrado")
        x = eval(input())
        y = x * x
        print("Resultado: ", y)
    except ValueError:
        print("Digite apenas números!")


ladoquadrado()
