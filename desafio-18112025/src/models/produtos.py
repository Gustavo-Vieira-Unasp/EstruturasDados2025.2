# Estrutura da Lista:

# Cada nó representa um item da lista com:
# Nome do produto
# Quantidade
# Categoria (alimentos, limpeza, higiene, etc.)
# Prioridade (alta, média, baixa)
# Status (pendente, comprado)
# Data de inclusão
from No.no import No




class Produto:
    def __init__(self, nome, quantidade, categoria, prioridade, status, data_inclusao):
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
        self.prioridade = prioridade  
        self.status = status
        self.data_inclusao = data_inclusao
        
        self.historico = Historico()
        

class Registro:
    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.proximo = None


class Historico:
    def __init__(self):
        self.historico = None

    def adicionar(self, msg):
        novo = Registro(msg)
        novo.proximo = self.historico
        self.historico = novo



    