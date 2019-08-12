# 8. Receba o valor de um depósito em poupança. Calcule e mostre o valor
# após 1 mês de aplicação sabendo que rende 1,3% a. m.


def poupanca():
    try:
        deposito = int(input("Digite o valor da poupança: "))
        deposito = deposito + (deposito *0.013)
        print(deposito)
    except ValueError:
        print("Digite apenas números!")

poupanca()
