# QUESTÃO 07 - Faça um programa que receba a idade de várias pessoas e que para cada uma, calcule e mostre:
# - a quantidade de pessoas com idade maior ou igual a 18;
# - a quantidade de pessoas com idade menor que 18.

idade = 0
continuar = "Sim"
maiores18 = 0
menores18 = 0
quantidadePessoas = 0

while continuar.upper() == "SIM":
    idade = int(input("Digite uma idade:"))

    if idade >= 18:
        maiores18 += 1
    
    else:
        menores18 += 1

    quantidadePessoas += 1
    continuar = input("Deseja continuar? (SIM/ NÃO): ")
    
print("Total de pessoas:", quantidadePessoas)
print("Maiores de 18 anos:", maiores18)
print("Menores de 18 anos:", menores18)

