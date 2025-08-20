# bibliotecas e frameworks
from datetime import date, timedelta
from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel, EmailStr
from database import get_db_session
from models import Aluno
from schemas import AlunoResponse, AlunoRequest

import logging

logger = logging.getLogger(__name__)

# criou o objeto de roteamento
router = APIRouter()

# banco de dados simulado (fake)
alunos_db = {
    "joao@iterasys.com.br": {
        "nome": "João Cruz",
        "validade_assinatura": "2025-12-31"
    },
        "maria@iterasys.com.br": {
        "nome": "Maria Oliveira",
        "validade_assinatura": "2026-05-15"
    }
}

# class AlunoRequest(BaseModel):
#     email: EmailStr

# @router.post("/")
# def buscar_aluno_post(dados: AlunoRequest):
#     aluno = alunos_db.get(dados.email)
#     logger.info(f"Consulta realizada para: {dados.email}")
#     if not aluno:
#         raise HTTPException(status_code=404, detail="Aluno não encontrado")
#     return aluno

# @router.get("/")
# def buscar_aluno_get(email: EmailStr):
#     aluno = alunos_db.get(email)
#     logger.info(f"Consulta realizada para: {email}")
#     if not aluno:
#         raise HTTPException(status_code=404, detail="Aluno não encontrado")
#     return aluno

@router.post("/", response_model=AlunoResponse, 
             status_code=201, response_description="Aluno Criado")
async def criar_aluno(aluno: AlunoRequest, db: AsyncSession = Depends(get_db_session)):
    # lê a data atual e projeta a data final da assinatura daqui há um ano
    validade_assinatura = date.today() + timedelta(days=365)
    # prepara a estrutura de dados para cadastrar o novo aluno
    novo_aluno = Aluno(
        nome=aluno.nome,
        email=aluno.email,
        senha_hash=aluno.senha,
        validade_assinatura=validade_assinatura
    )
    # Tenta criar o novo aluno banco de dados
    try:
        db.add(novo_aluno)
        await db.commit()
        await db.refresh(novo_aluno)

    # Se der algo errado, vai desfazer a transação inteira (os 3 passos acima)
    except Exception as e:
        await db.rollback() 
        raise HTTPException(status_code=500, detail="Erro ao salvar o aluno")
    print(novo_aluno) # exibir dados no aluno
    return novo_aluno

@router.get("/", response_model=AlunoResponse)
async def buscar_aluno(email: EmailStr, db: AsyncSession = Depends(get_db_session)):
    # executa a consulta no banco de dados
    result = await db.execute(select(Aluno).filter(Aluno.email == email))
    aluno = result.scalars().first()
    logger.info(f"Consulta realizada para: {email}")
    if aluno is None:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno