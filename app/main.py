from fastapi import FastAPI
from .models.response import ResultadoSimulacao
from .game.simulador import Jogo

# instância da aplicação FastAPI
app = FastAPI(
    title="Simulador de Jogo de Tabuleiro",
    description="API que simula uma partida de um jogo de tabuleiro e retorna o vencedor.",
    version="1.0.0"
)

# Endpoint da API para executar a simulação
@app.get("/jogo/simular", response_model=ResultadoSimulacao, summary="Executa uma simulação completa")
async def simular_jogo():
    """
    Simulação o jogo com 4 jogadores de estratégias diferentes (impulsivo, exigente, cauteloso e aleatório)
    A simulação ocorre até que tenha apenas um jogador restante ou até que 1000 rodadas sejam completadas.

    Retorna:
    - **vencedor**: Estratégia do jogador vencedor
    - **jogadores**: Lista com as estratégias dos jogadores, ordenados pelo saldo final em ordem decrescente
    """
    simulador = Jogo()
    resultado = simulador.simular()
    return ResultadoSimulacao(**resultado)
