from .propriedade import Propriedade
from typing import List, TYPE_CHECKING
# evita importação circular
if TYPE_CHECKING:
    from .jogador import Jogador

class Tabuleiro:
    """
    Class para gerenciar as propriedades do jogo/tabuleiro
    """
    def __init__(self, num_propriedades: int = 20):
        self.propriedades = self._gerar_propriedades(num_propriedades)

    def _gerar_propriedades(self, quantidade: int) -> List[Propriedade]:
        """Gera uma lista de propriedades com custos e aluguéis variados."""
        lista_propriedades = []
        for i in range(quantidade):
            # logica utilizando PA (progressão aritmetica) para custos
            # ex.:
            # a 1ª propriedade (i=0): custo = 50 + (0 * 10) = 50
            # a 2ª propriedade (i=1): custo = 50 + (1 * 10) = 60
            # e assim por diante...
            custo = 50 + (i * 10)
            aluguel = custo * 0.25 # Aluguel é 25% do custo
            lista_propriedades.append(Propriedade(custo_venda=custo, valor_aluguel=int(aluguel)))
        return lista_propriedades
    
    def liberar_propriedades(self, jogador: 'Jogador'):
        """Libera todas as propriedades de um jogador eliminado."""
        for propriedade in self.propriedades:
            if propriedade.proprietario == jogador:
                propriedade.resetar()

    def resetar(self):
        """Reseta as propriedades do tabuleiro"""
        for propriedade in self.propriedades:
            propriedade.resetar()
