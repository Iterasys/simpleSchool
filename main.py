from contextlib import asynccontextmanager
from fastapi import FastAPI
from routers import aluno
import logging                  # biblioteca de registro

# Configuração do logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app:FastAPI):
    # inicialização da API  (ao ligar)
    logger.info("API Iniciada")

    yield # representa a aplicação enquanto executada

    # finalização da API    (ao desligar)
    logger.info("API Finalizada")      

app = FastAPI(lifespan=lifespan) # instancia o objeto do framework de criação de API

# @app.on_event("startup") # iniciar o logging
# def startup_event():
#     logger.info("API Iniciada")

# @app.on_event("shutdown") # finalizar o logging
# def shutdown_event():
#     logger.info("API Finalizada")

app.include_router(aluno.router, prefix="/buscar-aluno", tags=["Aluno"])