import os
from codigo.validacoes.validacao_transfereencia import validar_transferencia 
from codigo.transferir import transferir 
    
def transferencia(id_usuario):

    os.system("cls")

    conta_transferencia=input("Digite a conta para fazer a tranferencia:")

    if os.path.exists(f"usuarios\\{conta_transferencia}") == True:

        os.system("cls")

        valor_transferencia=input("Informe o valor inteiro para a transefrencia:")

        while valor_transferencia.isnumeric() == False:

            os.system("cls")

            print(f"{valor_transferencia} Invalido") 

            valor_transferencia=input("Informe o valor inteiro para a transefrencia:")        


        valor_transferencia=int(valor_transferencia)        

        os.system("cls")

        if validar_transferencia(id_usuario,valor_transferencia)== True:

            transferir(id_usuario,valor_transferencia,conta_transferencia)






            











    else:

        os.system("cls")

        print("Conta nao existente.")

        os.system("pause")


