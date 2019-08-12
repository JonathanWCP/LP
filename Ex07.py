# 7. Receba os valores do comprimento, largura e altura de um paralelepípedo.
# Calcule e mostre seu volume.


def paralelepipedo():
    try:
        c = int(input("Digite o comprimento do paralelepípedo: "))
        l = int(input("Digite a largura do paralelepípedo: "))
        h = int(input("Digite a altura do paralelepípedo: "))
        paral = c * l * h
        print("Resultado: ", paral)
    except ValueError:
        print("Digite apenas números!")


paralelepipedo()
