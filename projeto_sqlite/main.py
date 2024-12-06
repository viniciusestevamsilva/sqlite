import os
import sqlite3
import time
from crud import Exibir
from crud import Adicionar
from crud import Atualizar
from crud import Apagar

# Conectar ao banco de dado
conn = sqlite3.connect("C:/vinicius/sqlite/projeto_sqlite/aeroporto.db")
   
while True:
    os.system('cls') 
    print('+-----------------+          +-------------------+')
    print('| MENU COMANDOS   |          |      TABELAS      |')
    print('+-----------------+          +-------------------+')
    print('| 1 - Exibir      |          |   companhia_aerea |')
    print('| 2 - Adicionar   |          |      passageiro   |')
    print('| 3 - Atualizar   |          |  terminal_viagens |')
    print('| 4 - Apagar      |          |       ticket      |')
    print('| 5 - Finalizar   |          |                   |')
    print('+-----------------+          +-------------------+')

    opcao = input('Opção escolhida: ')

# ========================== FINALIZAÇÃO =============
    if opcao == '5':
        for i in range(0,3):
            os.system('cls')
            print('___________________________________________')
            print('|//////                                 12%|')
            time.sleep(2)
            os.system('cls')
            print('___________________________________________')
            print('|///////////                            22%|')
            time.sleep(2)
            os.system('cls')
            print('___________________________________________')
            print('|/////////////////                      40%|')
            time.sleep(2)
            os.system('cls')
            print('___________________________________________')
            print('|//////////////////////////             68%|')
            time.sleep(2)
            os.system('cls')
            print('___________________________________________')
            print('|///////////////////////////////        75%|')
            time.sleep(2)
            os.system('cls')
            print('___________________________________________')
            print('|////////////////////////////////////// 99%|')
            time.sleep(2)
            os.system('cls')
            print('Error de carregamento... Recomeçando')
            time.sleep(2)
            os.system('cls') 

        print('Carregamento concluido !')
        os.system('cls') 
        print('+--------------------------+')
        print('|    Programa finalizado   |')
        print('+--------------------------+')
        break


# ========================== EXIBIR =============
    elif opcao == '1':
        os.system('cls') 
        print('+---------------+')
        print('|    Exibindo   |')
        print('+---------------+')
        tabela = input('Digite o nome da tabela para exibir: ')
        
        if tabela == '' and tabela == int: # Ve se a tabela não esta vazia
            os.system('cls') 
            print('+---------------------------------+')
            print('| Opção inválida. Tente novamente.|')
            print('+---------------------------------+')
            input('|   Pressione ENTER para voltar   |')
            
        else:
            for i in range(0,3):
                os.system('cls') 
                print('Preparando recursos  @')
                time.sleep(2)
                os.system('cls') 
                print('Preparando recursos  . @')
                time.sleep(2)
                os.system('cls') 
                print('Preparando recursos  .. @')
                time.sleep(2)
                os.system('cls') 
                print('Preparando recursos  ... @')
                time.sleep(2)
            
            os.system('cls')
            exibir = Exibir()
            exibir.SELECT(tabela)
            print(f'| Exibindo a tabela: {tabela}')
            print('+------------------------------------+')
            input('|    Pressione ENTER para voltar     |')


# ========================== ADICIONAR =============
    elif opcao == '2':
        while True:  # Loop para continuar pedindo a adição
            os.system('cls') 
            print('+-------------------+')
            print('|    Adicionando    |')
            print('+-------------------+')
            tabela = input('Digite o nome da tabela para adicionar: ')
            
            # Verifica se são válidos e se não estão vazios
            if not tabela or not isinstance(tabela, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue
            
            else:
                adicionar = Adicionar()
                adicionar.INSERT(tabela)
                os.system('cls')
                exibir = Exibir()
                exibir.SELECT(tabela)
                print('|    Registro Adicionado com sucesso!  |')
                print('+--------------------------------------+')
                print('|        Deseja adicionar outro?       |')
                opcao = input('| - :')
            
                if opcao == 'n':
                    break 
                
                
# ========================== ATUALIZAR =============
    elif opcao == '3':
        while True: 
            os.system('cls') 
            print('+-------------------+')
            print('|    Atualizando    |')
            print('+-------------------+')
            tabela = input('Digite o nome da tabela para atualizar: ')
            
            # Verifica se são válidos e se não estão vazios
            if not tabela or not isinstance(tabela, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            identificador = input('Digite o identificador (ex: cpf ou id): ')
            
            if not identificador or not isinstance(identificador, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            valor = input(f'Digite o valor do {identificador} para atualizar: ')
            
            if not valor or not isinstance(valor, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('| Opção inválida. Tente novamente.|')
                print('+---------------------------------+')
                input('|   Pressione ENTER para voltar   |')
                continue

            atualizar = Atualizar()
            atualizar.UPDATE(tabela, identificador, valor)
            
            os.system('cls')
            exibir = Exibir()
            exibir.SELECT(tabela)
            print('|    Registro Atualizado com sucesso !  |')
            print('+---------------------------------------+')
            print('|        Deseja atualizar outro?        |')
            opcao = input('- :')
            if opcao == 'n':
                break 

    
# ==========================  APAGAR =============
    elif opcao == '4':
        while True:
            os.system('cls') 
            print('+----------------+')
            print('+    Apagando    +')
            print('+----------------+')
            tabela = input('Digite o nome da tabela para apagar: ')

            # Verificação se são válidos e se não estão vazios
            if not tabela or not isinstance(tabela, str):
                os.system('cls')
                print('+---------------------------------+')
                print('+ Opção inválida. Tente novamente.+')
                print('+---------------------------------+')
                input('Pressione ENTER para voltar')
                continue

            identificador = input('Digite o identificador (ex: cpf ou id): ')
            
            if not identificador or not isinstance(identificador, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('+ Opção inválida. Tente novamente.+')
                print('+---------------------------------+')
                input('Pressione ENTER para voltar')
                continue

            valor = input(f'Digite o valor do {identificador} para apagar: ')
            
            if not valor or not isinstance(valor, str):
                os.system('cls') 
                print('+---------------------------------+')
                print('+ Opção inválida. Tente novamente.+')
                print('+---------------------------------+')
                input('Pressione ENTER para voltar')
                continue
            
            apagar = Apagar()
            apagar.DELETE(tabela, identificador, valor)
            os.system('cls')
            exibir = Exibir()
            exibir.SELECT(tabela)
            print('+    Registro apagado com sucesso !  +')
            print('+------------------------------------+')
            print('+        Deseja apagar outro?        +')
            opcao = input('- :')
            if opcao == 'n':
                break 

    
# ========================== OPÇÃO INVALIDA =============
    else:
        os.system('cls') 
        print('+---------------------------------+')
        print('| Opção inválida. Tente novamente.|')
        print('+---------------------------------+')
        input('|   Pressione ENTER para voltar   |')