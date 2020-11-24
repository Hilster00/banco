#mudar senha
import os
from codigo.validacao import validacao
from codigo.importar_ctrl_c import erro_ctrl


def mudar_senha(id):

    os.system("cls")

    senha=erro_ctrl("Digite a sua antiga senha:")

    senha_atual=open(f"usuarios\\{id}\\senha.txt", "r")

    senha_atual_limpa=senha_atual.readlines()

    senha_atual_limpa=senha_atual_limpa[0]

    senha_atual.close()

    nova_senha=""

    nova_senha_confirmar=""

    mensagem=""

    while len(nova_senha) < 5:

        os.system("cls")

        print(mensagem)

        nova_senha=erro_ctrl("Digite a nova senha:")

        mensagem="senha muito curta"

    mensagem=""

    while len(nova_senha_confirmar) < 5:

        os.system("cls")

        print(mensagem)

        nova_senha_confirmar=erro_ctrl("Confirmar a nova senha")

        mensagem="senha muito curta"
    
    if nova_senha == nova_senha_confirmar and nova_senha != senha_atual_limpa:

        senha_atual=open(f"usuarios\\{id}\\senha.txt", "w")

        senha_atual.write(f"{nova_senha}")

        os.system("cls")

        print("Nova senha confirmada")

    else:

        os.system("cls")

        print("Não foi possivel mudar a senha")
    
    os.system("pause")