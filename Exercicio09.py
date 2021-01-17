# QUESTÃO 09 - Faça um algoritmo para ler um número que é um código de usuário. Caso este código seja
# diferente de um código armazenado internamente no algoritmo (igual a 1234) deve ser apresentada a 
# mensagem ‘Usuário inválido!’. Caso o Código seja correto, deve ser lido outro valor que é a senha. 
# Se esta senha estiver incorreta (a certa é 9999) deve ser mostrada a mensagem ‘senha incorreta’. 
# Caso a senha esteja correta, deve ser mostrada a mensagem ‘Acesso permitido’. O usuário pode tentar 
# até 5 vezes. Após a 5a tentativa, deve ser exibida a mensagem “Usuário Bloqueado”.

codigoUsuario = 0
senhaUsuario = 0
contadorTentativas = 5

while contadorTentativas != 0:

    codigoUsuario = int(input("Digite o código de usuário: "))

    if codigoUsuario == 1234:
        senhaUsuario = int(input("Digite a senha: "))

        if senhaUsuario == 9999:
            print("Acesso permitido!")
            break
        else:
            print("Senha Incorreta!")
            contadorTentativas -= 1
    
    else:
        print("Usuário Inválido!")

if contadorTentativas == 0:
    print("Usuário bloqueado! Número de tentativas excedido.")