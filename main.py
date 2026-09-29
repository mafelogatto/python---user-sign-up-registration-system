# 'os' module
import os

print("--- SISTEMA DE CADASTRO DE USUÁRIOS ---")

# variables and constants
NOME_ARQUIVO = "usuarios.csv"
invalido = 0  #counter for invalid requests
max_tentativas = 3

# verifying if the arquive already exists
existe = os.path.exists(NOME_ARQUIVO)
if existe:
    arquivo = open(NOME_ARQUIVO, "a")
else:
    arquivo = open(NOME_ARQUIVO, "a+") #if it doesn't exist, we're able to create one through a+

# if it didnt exist before - therefore just got created - we're able to make a header
if not existe:
    arquivo.write(f"Nome,Idade,Perfil\n")

# main loop
while True:
    print("--- CADASTRAR NOVO USUÁRIO ---")
    print('1 - Entrada de dados via terminal')
    opcao = input('Escolha uma opção: 0 - Encerrar, 1 - Cadastrar: ')

    # structure conditionals on menu 
    if opcao == "0":
        print('Cadastro foi encerrado')
        break

    elif opcao == "1":
        print('Iniciando o cadastro')

        nome = input('Digite seu nome: ')
        idade = input('Digite sua idade: ')

        # second loop - profile validation
        tentativas_perfil = 0
        while True:
            tipo = input('Digite seu perfil (Admin/Usuário): ')

            if tipo.lower() == "admin" or tipo.lower() == "usuario":
                tipo = tipo.capitalize() # to set a patern
                break  # if valid, the profile leaves the loop
            else:
                tentativas_perfil += 1

                # verifying if profile sign up tries and fails limit has been hit, causing the user to be register as a regular
                if tentativas_perfil == max_tentativas:
                    print('Você não possui mais tentativas de perfil, por isso ficará como Usuário')
                    tipo = "Usuário"
                    break
                else:
                    # try ups counter in case theres still any left
                    print(f'Valor inserido inválido. Você possui mais {max_tentativas - tentativas_perfil} tentativa(s).')

  
        # a few strips for better organization
        nome = nome.strip()
        idade = idade.strip()
        tipo = tipo.strip()

        # saving the data on CSV
        arquivo.write(f"{nome},{idade},{tipo}\n")
        print(f"Usuário {nome} salvo com sucesso!")

    else:
        # structure to deal with inexistent inputs at the main menu
        invalido += 1
        if invalido == max_tentativas:
            print('Você atingiu o máximo de tentativas no menu.')
            break
        else:
            print(f'Valor inserido inválido, tente novamente. Você possui mais {max_tentativas - invalido} tentativa(s).')

# arquive closure
if arquivo is not None:
    arquivo.close()

print('Programa encerrado')
