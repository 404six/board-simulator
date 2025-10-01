from fastapi import FastAPI

# Cria a instância da aplicação FastAPI
app = FastAPI(
    title="Simulador de Jogo de Tabuleiro",
    description="API para simular uma partida de Banco Imobiliário e determinar o vencedor.",
    version="1.0.0"
)
