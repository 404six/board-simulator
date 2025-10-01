# Guia de Execução - Simulador de Jogo de Tabuleiro

Este documento fornece um passo a passo para configurar e executar a aplicação da simulação do jogo.

## Visão Geral da Estrutura

O projeto está organizado da seguinte forma para seguir as boas práticas de desenvolvimento e facilitar a manutenção:

* `app/`: Contém todo o código fonte da aplicação.
  * `game/`: Lógica central do jogo.
  * `models/`: Modelos de dados Pydantic para a API.
  * `main.py`: O ponto de entrada da API FastAPI.
* `tests/`: Contém os testes unitários.
* `Dockerfile`: Define a receita para construir a imagem Docker da aplicação.
* `docker-compose.yml`: Orquestra a execução do contêiner Docker.
* `requirements.txt`: Lista as dependências Python do projeto.

## Pré-requisitos

* Python 3.9+
* Docker e Docker Compose

## Opção 1: Executando com Docker (Recomendado)

Esta é a maneira mais fácil e padronizada de executar a aplicação.

### Passo 1: Iniciar a Aplicação

Navegue até a pasta raiz do projeto (onde o arquivo `docker-compose.yml` está localizado) e execute o comando:

```bash
docker-compose up --build
```

* `--build`: Garante que a imagem Docker seja construída na primeira vez ou caso o `Dockerfile` tenha sido alterado.

O Docker irá construir a imagem e iniciar o contêiner.

### Passo 2: Acessar a API

A aplicação estará rodando. Você pode testar o endpoint de simulação usando `curl` no seu terminal ou acessando a URL no navegador.

**Com `curl`:**

```bash
curl http://localhost:8080/jogo/simular
```

**Com navegador:**

Abra o seu navegador e acesse a documentação interativa (gerada automaticamente pelo FastAPI) no endereço:

[http://localhost:8080/docs](http://localhost:8080/docs)

A partir dessa página, você pode executar o endpoint `/jogo/simular` e ver a resposta.

### Passo 3: Parar a Aplicação

Para parar o contêiner, pressione `Ctrl + C` no terminal onde o `docker-compose` está rodando.

## Opção 2: Executando Localmente (Sem Docker)

Se preferir não usar Docker, siga estes passos.

### Passo 1: Criar um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

### Passo 2: Instalar as Dependências

```bash
pip install -r requirements.txt
```

### Passo 3: Iniciar o Servidor

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8080
```

## Executando os Testes

Para garantir que a lógica do jogo está funcionando corretamente, você pode executar a suíte de testes com `pytest`.

```bash
pytest
```