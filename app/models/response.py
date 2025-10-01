from pydantic import BaseModel, Field
from typing import List

class ResultadoSimulacao(BaseModel):
    """
    Define a estrutura de dados para a resposta da simulação do jogo.
    """
    vencedor: str = Field(..., example="cauteloso", description="O comportamento do jogador q venceu.")
    jogadores: List[str] = Field(..., example=["cauteloso", "aleatorio", "exigente", "impulsivo"], description="lista de jogadores ordenada pelo saldo final.")