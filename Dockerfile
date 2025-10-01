FROM python:3.11-slim

WORKDIR /app

# ---- dependencies stage ----
COPY requirements.txt .

# instala as dependências do projeto.
RUN pip install --no-cache-dir --upgrade pip -r requirements.txt

# ---- application stage ----
COPY ./app /app/app

EXPOSE 8080

# comando para executar a aplicação quando o container iniciar.
# utiliza uvicorn para rodar a aplicação FastAPI.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]

