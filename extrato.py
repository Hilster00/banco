#extrato
import os

def extrato(id_usuario):

    os.system("cls")

    dinheiro_conta=open(f"usuarios\\{id_usuario}\\dinheiro.txt","r")

    dinheiro_limpo=dinheiro_conta.readlines()

    dinheiro_limpo=float(dinheiro_limpo[0])

    dinheiro_conta.close()

    print(f"Voce possui R${dinheiro_limpo} na conta")

    print("\n"*15)

    os.system("pause")


