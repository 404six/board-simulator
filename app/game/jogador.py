from abc import ABC, abstractmethod
import random
from .propriedade import Propriedade

class Jogador(ABC):
    """
    Classe base abstrata para representar um jogador.
    Define os atributos e ações mais comuns a todos os jogadores.
    """
    def __init__(self, comportamento: str):
        self.comportamento = comportamento
        self.saldo = 0
        self.posicao = -1  # Começa fora do tabuleiro
        self.esta_jogando = True

    def resetar(self, saldo_inicial: int):
        """Reseta o jogador para o estado inicial de uma partida."""
        self.saldo = saldo_inicial
        self.posicao = -1
        self.esta_jogando = True
        
    def mover(self, passos: int, tamanho_tabuleiro: int):
        """Move o jogador no tabuleiro."""
        self.posicao = (self.posicao + passos) % tamanho_tabuleiro

    def creditar(self, valor: int):
        """Adiciona um valor ao saldo do jogador."""
        self.saldo += valor
        
    def debitar(self, valor: int):
        """Subtrai um valor do saldo do jogador."""
        self.saldo -= valor

    def pagar_aluguel(self, propriedade: Propriedade):
        """Paga o aluguel de uma propriedade ao dono."""
        valor_aluguel = propriedade.valor_aluguel
        self.debitar(valor_aluguel)
        propriedade.proprietario.creditar(valor_aluguel)

    def comprar_propriedade(self, propriedade: Propriedade):
        """Compra uma propriedade, atualizaa saldo e a posse."""
        self.debitar(propriedade.custo_venda)
        propriedade.proprietario = self

    def eliminar(self):
        """Define o jogador como eliminado."""
        self.esta_jogando = False
        
    @abstractmethod
    def decidir_compra(self, propriedade: Propriedade) -> bool:
        """
        Método abstrato que define a lógica de decisão de compra.
        Cada subclasse deve implementar sua própria estratégia.
        """
        pass