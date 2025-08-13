from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, UUID, String, Date

Base = declarative_base()

class Aluno(Base):
    __tablename__ = "aluno"

    id = Column(Integer, primary_key=True)
    nome = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    validade_assinatura = Column(Date, nullable=True)
    senha_hash = Column(String(255), nullable=True)

    def __repr__(self):
        return f"<Aluno(id={self.id}, nome='{self.nome}', email='{self.email}, validade_assinatura='{self.validade_assinatura}')>"
    