# 12. Receba o ano de nascimento e o ano atual. Calcule e mostre a sua idade e
# quantos anos terá daqui a 17 anos.


import datetime


def age():
    try:
        nasc = int(input("Digite o ano de nascimento: "))
        now = datetime.datetime.now()
        year = now.strftime('%Y')
        print("Você tem", int(year) - nasc)
        print("Você terá", (int(year) - nasc) + 17, "daqui há 17 anos")
    except ValueError:
        print("Digite apenas números inteiros!")


age()
