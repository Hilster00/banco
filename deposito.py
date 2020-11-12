#deposito
import os
from codigo.validacao import validacao


def deposito():

    autenticacao=validacao()

    id_usuario=autenticacao[1]

    autenticacao=autenticacao[0]  

    if autenticacao==True:       

        dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "r")

        dinheiro_limpo=dinheiro_usuario.readlines()

        dinheiro_usuario.close()

        dinheiro_limpo=int(dinheiro_limpo[0])

        while True:

            try:

                os.system("cls")

                valor_deposito=int(input("Digite o valor do deposito:"))

                break

            except:

                continue
        
        dinheiro_usuario=open(f"usuarios\\{id_usuario}\\dinheiro.txt", "w")

        dinheiro_limpo+=valor_deposito

        dinheiro_usuario.write(f"{dinheiro_limpo}")

        dinheiro_usuario.close()












