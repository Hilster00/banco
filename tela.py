import os

def tela_inicial():

    mensagem = ""

    while True:
        os.system("cls")

        print("SENHOR_H Banco, o banco mais confiavel e seguro")

        print(mensagem)

        print("(1) Loguin")

        print("\n")

        print("(2) Cadastro")

        print("\n")

        opcao=input("Digite a opcao desejada:")

        if opcao !="1" and opcao != "2":

            mensagem="Opcao invalida"

        else:

            break
    
    return opcao

def tela_usuario_logado():

    mensagem=""

    while True:

        os.system("cls")

        print(mensagem)

        print("(1) Operacoes bancarias")

        print("\n")

        print("(2) Configuracoes do Usuario")

        print("\n")

        opcao=input('Digite a opcao desejada:')

        if opcao != "1" and opcao != "2":

            mensagem=f'opcao "{opcao}" invalida\n'
        else:

            break

    return opcao

def tela_opcoes_bancarias():

    mensagem=""

    while True:

        os.system("cls")

        print(mensagem)

        print("(1) Saque")

        print("\n")

        print("(2) Deposito")

        print("\n")

        print("(3) Transferencia")

        print("\n")

        print("(4) Extrato Bancario")

        print("\n")

        print("(5) Sair")

        print("\n")

        opcao=input("Digite a opcao desejada:")

        opcoes=("1","2","3","4","5")

        if opcao not in opcoes:

            mensagem=f'Opcao "{opcao}" invalida'

        else:

            break
    
    return opcao

