from listaDeCompras.listaDeCompras import exibir_lista_de_compras

placeholder = []

def gerar_menu(placeholder):
    while True:
        print('''
            1 - Adicionar itens a lista
            2 - Remover itens da lista
            3 - Mudar prioridade
            4 - Exibir lista
              ''')
        
        acao_menu = input("Escolha a opção")

        if acao_menu == '1':
            return adicionar_itens
        
        elif acao_menu == '2':
            return remover_itens
        
        elif acao_menu == '3':
            return mudar_prioridade
        
        elif acao_menu == '4':
            return exibir_lista_de_compras(placeholder)