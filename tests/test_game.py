import sys
import os

# adiciona o diretório raiz do projeto ao sys.path para facilitar os imports relativos
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.game.jogador import JogadorImpulsivo, JogadorExigente, JogadorCauteloso, JogadorAleatorio
from app.game.propriedade import Propriedade
from app.game.simulador import Jogo

# --- Testes das Estratégias dos Jogadores ---

def test_jogador_impulsivo_decide_comprar():
    jogador = JogadorImpulsivo("teste")
    jogador.saldo = 200
    propriedade_cara = Propriedade(custo_venda=201, valor_aluguel=20)
    propriedade_barata = Propriedade(custo_venda=200, valor_aluguel=20)
    
    assert jogador.decidir_compra(propriedade_barata) is True
    assert jogador.decidir_compra(propriedade_cara) is False

def test_jogador_exigente_decide_comprar():
    jogador = JogadorExigente("teste")
    jogador.saldo = 200
    propriedade_aluguel_alto = Propriedade(custo_venda=150, valor_aluguel=51)
    propriedade_aluguel_baixo = Propriedade(custo_venda=150, valor_aluguel=50)
    
    assert jogador.decidir_compra(propriedade_aluguel_alto) is True
    assert jogador.decidir_compra(propriedade_aluguel_baixo) is False

def test_jogador_cauteloso_decide_comprar():
    jogador = JogadorCauteloso("teste")
    jogador.saldo = 180
    propriedade_ok = Propriedade(custo_venda=100, valor_aluguel=10) # Saldo restante: 80
    propriedade_nao_ok = Propriedade(custo_venda=101, valor_aluguel=10) # Saldo restante: 79

    assert jogador.decidir_compra(propriedade_ok) is True
    assert jogador.decidir_compra(propriedade_nao_ok) is False

def test_jogador_aleatorio_decide_comprar(mocker):
    jogador = JogadorAleatorio("teste")
    jogador.saldo = 100
    propriedade = Propriedade(custo_venda=100, valor_aluguel=10)
    
    # Mock para forçar o resultado da escolha aleatória
    mocker.patch('random.choice', return_value=True)
    assert jogador.decidir_compra(propriedade) is True
    
    mocker.patch('random.choice', return_value=False)
    assert jogador.decidir_compra(propriedade) is False

# --- Teste da Lógica de Eliminação ---

def test_eliminacao_de_jogador():
    jogo = Jogo()
    jogo._preparar_nova_partida()
    
    jogador_a_eliminar = jogo.jogadores[0]
    propriedade = jogo.tabuleiro.propriedades[0]

    # força a compra para associar uma propriedade ao jogador
    jogador_a_eliminar.saldo = 300
    jogador_a_eliminar.comprar_propriedade(propriedade)
    assert propriedade.proprietario == jogador_a_eliminar

    # Força a eliminação
    jogador_a_eliminar.saldo = -10
    jogo._jogar_turno(jogador_a_eliminar)

    assert jogador_a_eliminar.esta_jogando is False
    assert propriedade.proprietario is None # propriedade deve ser liberada

# --- Teste total de simulação ---

def test_simulacao_completa_retorna_resultado_valido():
    """
    Verifica se a simulação executa e retorna a estrutura de dados esperada.
    Não podemos prever o vencedor, mas podemos validar o formato.
    """
    jogo = Jogo()
    resultado = jogo.simular()

    assert "vencedor" in resultado
    assert "jogadores" in resultado
    assert isinstance(resultado["vencedor"], str)
    assert isinstance(resultado["jogadores"], list)
    assert len(resultado["jogadores"]) == 4
    # O vencedor deve estar na lista de jogadores
    assert resultado["vencedor"] in resultado["jogadores"]
