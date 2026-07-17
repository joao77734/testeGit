import random

print("Olá, como vc está coleguinha?")
print("Digite 1 para visualizar o comando de João:")

opcao = input()

if opcao == "1":

    print("\n=== PAR OU ÍMPAR ===")

    jogador = input("Escolha Par ou Ímpar (P/I): ").upper()
    numero = int(input("Digite um número de 0 a 10: "))

    computador = random.randint(0, 10)

    soma = numero + computador

    print("Computador escolheu:", computador)
    print("Soma:", soma)

    if soma % 2 == 0:
        resultado = "P"
    else:
        resultado = "I"

    if jogador == resultado:
        print("Você ganhou!")
    else:
        print("Você perdeu!")

    continuar = input("\nDeseja continuar para ver o próximo comando? (S/N): ").upper()

    if continuar == "N":
        print("Programa encerrado.")
    else:
        print("\nComando do Vinícius:")

        def subtração(n1, n2):
            result = n1 - n2
            print("O resultado dos numeros", n1, "e", n2, "é:", result)

        n1 = int(input("Digite um número para subtrair:\n"))
        n2 = int(input("Digite o segundo número para subtrair:\n"))

        subtração(n1, n2)

        print("\nEspero q tenha gostado!")