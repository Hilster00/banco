#cadastro

import os

def cadastrar():

    informacoes=["nome do usuario","cpf","senha"]

    quantidade_caracteres=[2,11,5]

    tipo_da_informacao_texto=[True,False]

    novo_usuario={}

    os.system("cls")

    while True:


        novo_usuario["idade"]=input("Informe a sua idade:")

        if novo_usuario["idade"].isnumeric() == True:

            novo_usuario["idade"]=int(novo_usuario["idade"])

            break
        else:

            os.system("cls")

            print(f'Idade ({novo_usuario["idade"]}) invalido')

    if novo_usuario["idade"] >= 18:

        os.system("cls")

        for iten in informacoes:

            while True:        
            
                novo_usuario[iten]=input(f"Informe o {iten} do novo usuario:")

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

        while True:

            id="id"

            novo_usuario[id]=input("Informe um id de acesso:")            

            nova_pasta_usuario=novo_usuario[id]

            if os.path.exists(f"usuarios\\{nova_pasta_usuario}") == False:                

                os.system(f"mkdir usuarios\\{nova_pasta_usuario}")

                break

            else:

                os.system("cls")

                print(f"o id {nova_pasta_usuario} ja esta em uso, escolha outro")

        #____________________________________________________________________________________

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

        cpf_usuario.write(novo_usuario["cpf"][0:10])

        cpf_usuario.close()

    else:

        os.system("cls")

        print("Lamento, mas so maiores de 18 podem fazer uma conta nesse banco!")



    

    

    


