#extrato
from codigo.validacao import validacao
import os

def extrato():

    autenticacao=validacao()

    id_usuario=autenticacao[1]

    autenticacao=autenticacao[0]

    if autenticacao == True:

        os.system("cls")

        dinheiro_conta=open(f"usuarios\\{id_usuario}\\dinheiro.txt","r")

        dinheiro_limpo=dinheiro_conta.readlines()

        dinheiro_limpo=int(dinheiro_limpo[0])

        dinheiro_conta.close()

        print(f"Voce possui R${dinheiro_limpo} na conta")

        print("\n"*15)

        os.system("pause")


