import random
from typing import Dict, List
from .jogador import Jogador, JogadorImpulsivo, JogadorExigente, JogadorCauteloso, JogadorAleatorio
from .tabuleiro import Tabuleiro

class Jogo:
    """
    Orquestra a simulação do jogo, gerenciando as rodadas, turnos e condições de vitória
    """
    MAX_RODADAS = 1000
    SALDO_INICIAL = 300

    def __init__(self):
        self.tabuleiro = Tabuleiro()
        self.jogadores = self._criar_jogadores()

    def _criar_jogadores(self) -> List[Jogador]:
        """Inicializa os 4 tipos de jogadores."""
        return [
            JogadorImpulsivo("impulsivo"),
            JogadorExigente("exigente"),
            JogadorCauteloso("cauteloso"),
            JogadorAleatorio("aleatorio")
        ]

    def _preparar_nova_partida(self):
        """Prepara o estado do jogo para uma nova simulação."""
        # limpa proprietários
        self.tabuleiro.resetar()
        
        # reseta cada jogador para o estado inicial
        for jogador in self.jogadores:
            jogador.resetar(self.SALDO_INICIAL)
            
        # define uma ordem aleatória de turnoss
        random.shuffle(self.jogadores)

    def _jogar_turno(self, jogador: Jogador):
        """Executa o turno de um jogador"""
        if not jogador.esta_jogando:
            return

        # joga o dado e move o jogador
        passos = random.randint(1, 6)
        posicao_anterior = jogador.posicao
        jogador.mover(passos, len(self.tabuleiro.propriedades))
        
        # verifica se completou uma volta
        if jogador.posicao < posicao_anterior:
            jogador.creditar(100)
            
        propriedade_atual = self.tabuleiro.propriedades[jogador.posicao]

        if propriedade_atual.proprietario and propriedade_atual.proprietario != jogador:
            # paga aluguel se a propriedade já tiver dono
            jogador.pagar_aluguel(propriedade_atual)
        elif not propriedade_atual.proprietario:
            # decide se compra a propriedade caso não tenha dono
            if jogador.decidir_compra(propriedade_atual):
                jogador.comprar_propriedade(propriedade_atual)
        
        # elimina o jogador por saldo negativo
        if jogador.saldo < 0:
            jogador.eliminar()
            self.tabuleiro.liberar_propriedades(jogador)

    def simular(self) -> Dict:
        pass