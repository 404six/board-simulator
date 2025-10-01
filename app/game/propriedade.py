class Propriedade:
    """
    Representa uma propriedade no tabuleiro
    """
    def __init__(self, custo_venda: int, valor_aluguel: int):
        self.custo_venda = custo_venda
        self.valor_aluguel = valor_aluguel
        self.proprietario = None

    def resetar(self):
        """reseta o proprietário"""
        self.proprietario = None
