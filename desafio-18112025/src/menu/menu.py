from src.listaEncadeada.listaEncadeada import ListaEncadeada
from listaDeCompras.listaDeCompras import exibir_lista_de_compras

def gerar_menu(placeholder : ListaEncadeada):
    while True:
        print('''
            1 - Adicionar itens a lista
            2 - Remover itens da lista
            3 - Mudar prioridade
            4 - Exibir lista
              ''')
        
        acao_menu = input("Escolha a opção")

        if acao_menu == '1':
            return adicionarItens(placeholder)
        
        elif acao_menu == '2':
            return removerItens(placeholder)
        
        elif acao_menu == '3':
            return mudarPrioridade(placeholder)
        
        elif acao_menu == '4':
            return exibir_lista_de_compras(placeholder)
        
def adicionarItens(placeholder : ListaEncadeada):
    
    pass

def removerItens(placeholder : ListaEncadeada):
    pass

def mudarPrioridade(placeholder : ListaEncadeada):
    pass