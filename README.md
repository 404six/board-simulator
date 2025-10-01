# Simulador de Jogo de Tabuleiro com FastAPI

Este projeto é uma API desenvolvida em Python que simula uma partida de um jogo de tabuleiro (semelhante ao Banco Imobiliário), com regras simples e diferentes estratégias de jogadores.

## Como o Projeto Foi Feito

A arquitetura foi pensada para ser limpa, escalável e de fácil manutenção, seguindo boas práticas de desenvolvimento de software.

1. **Separação de Responsabilidades**: A lógica central do jogo (`app/game`) é completamente desacoplada da camada de API (`app/main.py`). Isso significa que o motor da simulação poderia ser reutilizado em qualquer outro contexto (uma aplicação de linha de comando, um bot, etc.) sem qualquer alteração.

2. **Programação Orientada a Objetos (OOP)**: O domínio foi modelado com classes: `Jogo`, `Tabuleiro`, `Propriedade` e `Jogador`. A classe `Jogador` foi definida como uma classe base abstrata, o que permitiu implementar diferentes estratégias (`Impulsivo`, `Exigente`, etc.) de forma organizada.

3. **Desenvolvimento Guiado por Testes (TDD)**: A lógica foi validada com testes unitários (`tests/`). Garantindo que as regras do jogo e as estratégias dos jogadores funcionem como é esperado, além de prever possiveis tratamento de casos.

4. **Conteinerização com Docker**: Encapsulando a aplicação e as dependências, garantindo um ambiente de execução consistente e simplificando bastante o processo de deploy e execução do app.

## Tecnologias Utilizadas

* **Linguagem**: Python 3.11

* **Framework para API**: FastAPI

* **Validação de Dados**: Pydantic

* **Servidor ASGI**: Uvicorn

* **Testes**: Pytest

* **Conteinerização**: Docker (e Docker Compose)

## Como Executar

Para um guia detalhado de como rodar a aplicação, é só acessar o arquivo [COMMENTS.md](COMMENTS.md).