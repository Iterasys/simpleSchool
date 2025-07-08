# bibliotecas e frameworks
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr

# criou o objeto da API
app = FastAPI()

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

@app.post("/buscar-aluno")
def buscar_aluno(dados: AlunoRequest):
    aluno = alunos_db.get(dados.email)
    if not aluno:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return {
        "nome_completo": aluno["nome"],
        "validade_assinatura": aluno["validade_assinatura"]
    }
