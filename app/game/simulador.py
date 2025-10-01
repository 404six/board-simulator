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
        """
        Simula uma partida completa do jogo.
        """
        self._preparar_nova_partida()
        
        for rodada in range(self.MAX_RODADAS):
            for jogador in self.jogadores:
                self._jogar_turno(jogador)

            jogadores_ativos = [j for j in self.jogadores if j.esta_jogando]
            if len(jogadores_ativos) == 1:
                # condição de vitória: apenas um jogador restante
                vencedor = jogadores_ativos[0]
                break
        else:
            # condição de vitória: fim das 1000 rodadas (vence quem tem mais saldo)
            vencedor = max(self.jogadores, key=lambda j: j.saldo)
        
        # ordena os jogadores por saldo para o resultado final
        jogadores_ordenados = sorted(self.jogadores, key=lambda j: j.saldo, reverse=True)
        
        return {
            "vencedor": vencedor.comportamento,
            "jogadores": [j.comportamento for j in jogadores_ordenados]
        }
