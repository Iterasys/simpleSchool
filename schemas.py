from pydantic import BaseModel, ConfigDict, EmailStr
from datetime import date

class AlunoRequest(BaseModel):
    nome: str
    email: EmailStr
    senha: str

class AlunoResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    id: int
    nome: str
    email: EmailStr
    validade_assinatura: date
