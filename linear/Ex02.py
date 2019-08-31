# 2. Receba o salário de um funcionário e mostre o novo salário com reajuste
# de 15%.


def reajuste_salario():
    try:
        x = eval(input("Digite o salario: "))
        y = x+ x*0.15
        print("Novo salario: ", y)
    except ValueError:
        print("Digite apenas números!")


reajuste_salario()
