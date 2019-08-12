# 6. Receba os valores em x e y. Efetua a troca de seus valores e mostre seus
# conteúdos.


def troca():
    try:
        x = int(input("Digite o valor de X: "))
        y = int(input("Digite o valor de Y: "))
        x, y = y, x
        print("O novo valor de X é", x, "e o de Y é", y)
    except ValueError:
        print("Digite apenas números inteiros!")


troca()
