from codigo.cadastrar import cadastrar
from codigo.telas.tela_inicial import tela_inicial
from codigo.loguin import loguin
from codigo.usuario import usuario
import os

if os.path.exists("usuarios")== False:
    os.system("mkdir usuarios")

while True:
    
    os.system("title SENHOR_H BANCO ")

    opcao=tela_inicial()

    if opcao == "1":

        if os.listdir("usuarios\\") != []:

            id=loguin()

            if id[0] == True:

                break

        else:

            os.system("cls")

            print("Sem usuarios cadastrados")

            print("\n")

            os.system("pause")

            continue


    else:
        
        cadastrar()

usuario(id[1])
