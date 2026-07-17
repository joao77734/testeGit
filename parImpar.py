#sistema Par ou Ímpar
import random

print("=== PAR OU ÍMPAR ===")

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