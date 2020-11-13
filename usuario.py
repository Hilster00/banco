#usuario
import os
from codigo.tela import tela_usuario_logado
from codigo.tela import tela_opcoes_bancarias
from codigo.transferencia import transferencia
from codigo.extrato import extrato
from codigo.deposito import deposito
from codigo.saque import saque


def usuario():

    while True:
    
        opcao=tela_usuario_logado()

        if opcao == "1":

            opcao=tela_opcoes_bancarias()

            if opcao =="1":

                saque()

            elif opcao == "2":

                deposito()

            elif opcao == "3":    

                if len(os.listdir("usuarios\\")) != 1:

                    transferencia()                 

                else:

                    os.system("cls")

                    print("Nao existe outra conta para faer transferencia")

                    os.system("pause")
        
            elif opcao =="4":            

                extrato()

            elif opcao == "5":

                break




