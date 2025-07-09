# bibliotecas e frameworks
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr
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

class AlunoRequest(BaseModel):
    email: EmailStr

@router.post("/")
def buscar_aluno_post(dados: AlunoRequest):
    aluno = alunos_db.get(dados.email)
    logger.info(f"Consulta realizada para: {dados.email}")
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno

@router.get("/")
def buscar_aluno_get(email: EmailStr):
    aluno = alunos_db.get(email)
    logger.info(f"Consulta realizada para: {email}")
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno