# Estrutura da Lista:

# Cada nó representa um item da lista com:
# Nome do produto
# Quantidade
# Categoria (alimentos, limpeza, higiene, etc.)
# Prioridade (alta, média, baixa)
# Status (pendente, comprado)
# Data de inclusão



class Produto:
    prioridade_valor = {
        "alta": 1,
        "media": 2,
        "baixa": 3
    }

    def __init__(self, nome, quantidade, categoria, prioridade, status, data_inclusao):
        self.nome = nome
        self.quantidade = quantidade
        self.categoria = categoria
        self.prioridade = prioridade
        self.status = status
        self.data_inclusao = data_inclusao
        
        self.prioridade_indice = Produto.prioridade_valor[prioridade]
        self.historico = Historico()

    def registrar(self, msg):
        self.historico.adicionar(msg)

    def alterar_prioridade(self, nova_prioridade):
        self.registrar(f"Prioridade alterada de {self.prioridade} para {nova_prioridade}")
        self.prioridade = nova_prioridade
        self.prioridade_indice = Produto.prioridade_valor[nova_prioridade]

        

class Registro:
    def __init__(self, mensagem):
        self.mensagem = mensagem
        self.proximo = None


class Historico:
    def __init__(self):
        self.cabeça= None

    def adicionar(self, msg):
        novo = Registro(msg)
        novo.proximo = self.cabeça
        self.cabeça = novo



def inserir_ordenado(self, produto):
    novo = No(produto)

    # se a lista está vazia ou prioridade do novo é maior (1 é melhor que 2,3)
    if not self.cabeça or produto.prioridade_indice < self.cabeça.valor.prioridade_indice:
        novo.proximo = self.cabeça
        self.cabeça = novo
        return

    atual = self.cabeça
    while atual.proximo and atual.proximo.valor.prioridade_indice <= produto.prioridade_indice:
        atual = atual.proximo

    novo.proximo = atual.proximo
    atual.proximo = novo


    