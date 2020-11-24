#cadastro

import os
from codigo.importar_ctrl_c import erro_ctrl
from codigo.validacoes.validar_cpf import validar_cpf
from codigo.validacoes.validar_idade import validar_idade
from codigo.criar_id import criar_id
def cadastrar():

    informacoes=["nome do usuario","senha"]

    quantidade_caracteres=[2,5]

    tipo_da_informacao_texto=[True,False]

    novo_usuario={}

    os.system("cls")

    novo_usuario["idade"]=validar_idade()

    if novo_usuario["idade"] >= 18:

        os.system("cls")

        for iten in informacoes:

            while True: 

                print("\n")       
            
                novo_usuario[iten]=erro_ctrl(f"Informe o {iten} do novo usuario:")

                os.system("cls")

                if len(novo_usuario[iten]) < quantidade_caracteres[informacoes.index(iten)]:

                    print(f"Quantidade de digitos invalido\ndeve ter pelomenos {quantidade_caracteres[informacoes.index(iten)]} digitos")
                    
                else:
                    
                    if iten != "senha":

                        if novo_usuario[iten].isalpha() == tipo_da_informacao_texto[informacoes.index(iten)]:

                            break

                        os.system("cls")

                        print(f"{novo_usuario[iten]} invalido como {iten}")
                    else:

                        break

        os.system("cls")

        novo_usuario["cpf"]=validar_cpf()

        while True:

            novo_id=criar_id()

            

            if os.path.exists(f"usuarios\\{novo_id}") == False:

                break

                
        nova_pasta_usuario=novo_id.upper()
        
        os.system("cls")

        while True:

            nome=novo_usuario["nome do usuario"].title()

            try:
        
                confirmar=(erro_ctrl(f"Confirma o novo cadastro do {nome} (S/N):")).lower()

                confirmar=confirmar[0]

            except:

                os.systen("cls")

                print("Opção invalida")

                print("\n")

                continue

            if confirmar != "s" and confirmar != "n":

                os.system("cls")

                print("Opção invalida")

                print("\n")
            else:

                if confirmar[0].lower() == "s":
                    
                    os.system(f"mkdir usuarios\\{nova_pasta_usuario}")

                    #____________________________________________________________________________________
                    try:
                        nome_usuario=open(f"usuarios\\{nova_pasta_usuario}\\nome.txt", "a")

                        nome_usuario.write(novo_usuario["nome do usuario"].title())

                        nome_usuario.write(f"\n{novo_usuario['idade']}")

                        nome_usuario.close()


                        #____________________________________________________________________________________

                        senha_usuario=open(f"usuarios\\{nova_pasta_usuario}\\senha.txt", "a")

                        senha_usuario.write(novo_usuario["senha"])

                        senha_usuario.close()

                        #____________________________________________________________________________________

                        dinheiro_usuario=open(f"usuarios\\{nova_pasta_usuario}\\dinheiro.txt", "a")

                        dinheiro_usuario.write("0")

                        dinheiro_usuario.close()

                        #____________________________________________________________________________________

                        cpf_usuario=open(f"usuarios\\{nova_pasta_usuario}\\cpf.txt", "a")

                        cpf_usuario.write(novo_usuario["cpf"])

                        cpf_usuario.close()                    

                        mensagem=f"Usuario {nome} cadastrado com sucesso.\nSeu id é {novo_id.upper()}"
                    
                    except:

                        mensagem=f"Usuario {nome} não foi criado com sucesso."

                else:

                    mensagem=f"Usuario {nome} não foi criado."

                break

        os.system("cls") 

        print(mensagem)

        os.system("pause")

    else:

        os.system("cls")

        print("Lamento, mas so maiores de 18 podem fazer uma conta nesse banco!")

        os.system("pause")



    

    

    


