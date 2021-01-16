# QUESTÃO 06 - Crie um programa para fazer a chamada e contar a quantidade de pessoas em um recinto.
# O programa deve perguntar “Tem mais alguém presente?”. Enquanto a resposta for correspondente a Sim, 
# a quantidade de pessoas deve ser incrementada. No final, deve-se imprimir a quantidade de pessoas presentes.

chamada = input("Há mais alguém presente? ")
contagemPessoas = 0

while chamada.upper() == "SIM":
    contagemPessoas += 1
    chamada = input("Há mais alguém presente? ")
    
print(f"Há {contagemPessoas} pessoas presentes!")