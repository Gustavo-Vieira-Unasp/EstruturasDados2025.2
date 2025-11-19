# Estrutura da Lista:

# Cada nó representa um item da lista com:
# Nome do produto
# Quantidade
# Categoria (alimentos, limpeza, higiene, etc.)
# Prioridade (alta, média, baixa)
# Status (pendente, comprado)
# Data de inclusão
from no import No


class Produto:
    def __init_(self, nome, quantidade, categoria, prioridade, status, data_inclusao):
        self.Nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
        self.prioridade = prioridade
        self.status = status
        self.data_inclusao = data_inclusao

 