import sys
# meu_numero = 0
# while meu_numero < 42:
#     meu_numero += int(input("Digite seu numero:"))
# print("A soma dos seus numeros superou 42")


if __name__ == "__main__":
    for argument in sys.argv:
        print("Received -> ", argument)

