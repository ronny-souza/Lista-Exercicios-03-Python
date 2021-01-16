# QUESTÃO 04 - Faça um programa que receba a idade e o sexo (Masculino, Feminino ou Não Quero Declarar) 
# de oito pessoas e que calcule a média das idades e a quantidade de pessoas de cada sexo.
idade = []
sexo = []
quantidadePessoas = 0
masculino = 0
feminino = 0
naoDeclarado = 0
somaIdades = 0
mediaIdades = 0

for i in range(8):
    idade.append(int(input("Digite a sua idade: ")))
    sexo.append(input("Digite seu sexo (Masculino/Feminino/Não quero declarar): "))

    if sexo[i].upper() == "MASCULINO":
        masculino += 1
    
    elif sexo[i].upper() == "FEMININO":
        feminino += 1
    
    elif sexo[i].upper() == "NÃO QUERO DECLARAR":
        naoDeclarado += 1
    
    else:
        print("Sexo inválido!")
    
    quantidadePessoas += 1
    somaIdades += idade[i]

mediaIdades = (somaIdades / quantidadePessoas)
print("***** INFORMAÇÕES *****")
print("Total de pessoas: ", quantidadePessoas)
print("Quantidade de Homens: ", masculino)
print("Quantidade de Mulheres: ", feminino)
print("Quantidade de pessoas que não declararam sexo: ", naoDeclarado)
print("Média de Idades: ", mediaIdades)
