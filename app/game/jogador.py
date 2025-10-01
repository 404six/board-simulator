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
        Método abstrato para definir a lógica de decisão de compra.
        Cada subclasse irá implementar sua própria estrategia
        """
        pass

# --- Estratégias ---
class JogadorImpulsivo(Jogador):
    """Compra qualquer propriedade (se tiver saldo)."""
    def decidir_compra(self, propriedade: Propriedade) -> bool:
        return self.saldo >= propriedade.custo_venda

class JogadorExigente(Jogador):
    """Compra se o aluguel for maior que 50 e tiver saldo."""
    def decidir_compra(self, propriedade: Propriedade) -> bool:
        return propriedade.valor_aluguel > 50 and self.saldo >= propriedade.custo_venda

class JogadorCauteloso(Jogador):
    """Compra se, após a compra seu saldo restante for 80 ou mais"""
    def decidir_compra(self, propriedade: Propriedade) -> bool:
        return (self.saldo - propriedade.custo_venda) >= 80

class JogadorAleatorio(Jogador):
    """Compra com 50% de probabilidade se tiver saldo."""
    def decidir_compra(self, propriedade: Propriedade) -> bool:
        if self.saldo >= propriedade.custo_venda:
            return random.choice([True, False])
        return False