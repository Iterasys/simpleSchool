from fastapi import FastAPI
from routers import aluno
import logging                  # biblioteca de registro

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI() # instancia o objeto do framework de criação de API

@app.on_event("startup") # iniciar o logging
def startup_event():
    logger.info("API Iniciada")

@app.on_event("shutdown") # finalizar o logging
def shutdown_event():
    logger.info("API Finalizada")

app.include_router(aluno.router, prefix="/buscar-aluno", tags=["Aluno"])