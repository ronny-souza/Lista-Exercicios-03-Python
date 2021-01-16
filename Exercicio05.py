# QUESTÃO 05 - Crie um programa que receba vários valores numéricos e realize a multiplicação destes números.
# O algoritmo deve ser executado enquanto não for digitado o valor 0.

numero = int(input("Digite um número: "))
multiplica = 1

while numero != 0:

    multiplica *= numero
    numero = int(input("Digite um número: "))


print("Resultado da multiplicação: ", multiplica)
    