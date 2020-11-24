#usuario
import os
from codigo.validacao import validacao
from codigo.telas.tela_usuario_logado import tela_usuario_logado
from codigo.telas.tela_opcoes_bancarias import tela_opcoes_bancarias
from codigo.opcoes_bancarias.transferencia import transferencia
from codigo.opcoes_bancarias.extrato import extrato
from codigo.opcoes_bancarias.deposito import deposito
from codigo.opcoes_bancarias.saque import saque
from codigo.telas.tela_configuracoes_usuario import configuracoes_usuario
from codigo.telas.tela_alterar_informacoes import tela_alterar_informacoes
from codigo.mudar_idade import mudar_idade
from codigo.mudar_senha import mudar_senha
from codigo.importar_ctrl_c import erro_ctrl


def usuario(id):

    while True:
    
        opcao=tela_usuario_logado()

        if opcao == "1":

            while True:

                opcao=tela_opcoes_bancarias()

                if opcao != "5":                 

                    if validacao(id) == False:

                        continue

                if opcao =="1":

                    saque(id)

                elif opcao == "2":

                    deposito(id)

                elif opcao == "3":    

                    if len(os.listdir("usuarios\\")) != 1:

                        transferencia(id)                 

                    else:

                        os.system("cls")

                        print("Nao existe outra conta para faer transferencia")

                        os.system("pause")
            
                elif opcao =="4":            

                    extrato(id)

                elif opcao == "5":

                    break

        elif  opcao== "2":

            while True:

                opcao=configuracoes_usuario()

                if opcao=="1":

                    while True:

                        opcao=tela_alterar_informacoes()

                        if opcao == "1":

                            mudar_idade(id)

                        elif opcao == "2":

                            mudar_senha(id)                            
                        
                        else:

                            break


                            

                elif opcao == "2":

                    os.system("cls")                   

                    if validacao(id) == True:

                        while True:

                            confirmar=erro_ctrl("Deseja confirmar?(S/N):")

                            if len(confirmar) >= 1:

                                if (confirmar.lower())[0] == "s":

                                    os.system(f"rmdir usuarios\\{id} /s /q")

                                    print("Usuario foi removido com sucesso")

                                    os.system("pause")

                                    exit()

                                else:

                                    print("Cancelado")                   
                                
                else:

                    break
                
        else:

            exit()

