# 13. Receba a quantidade de alimento em quilos. Calcule e mostre quantos dias
# durará esse alimento sabendo que a pessoa consome 50g ao dia.


def diet():
    try:
        food = int(input("Digite a quantidade de alimento em quilos: "))
        result = food/0.50
        print("Essa quantidade durará", result, "dias")
    except ValueError:
        print("Digite apenas números!")


diet()
