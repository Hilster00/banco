from codigo.cadastrar import cadastrar
from codigo.tela import tela_inicial
from codigo.loguin import loguin
from codigo.usuario import usuario
import os

while True:
    os.system("title SENHOR_H BANCO ")

    opcao=tela_inicial()

    if opcao == "1":

        if os.listdir("usuarios\\") != []:

            if loguin() == True:

                break

        else:

            os.system("cls")

            print("Sem usuarios cadastrados")

            print("\n")

            os.system("pause")

            continue


    else:
        
        cadastrar()

usuario()
