from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

### Configuração do banco de dados para SQLAlchemy
DATABASE_URL = "sqlite+aiosqlite:///./database.db"

### Criar o engine assincrono
engine = create_async_engine(DATABASE_URL, echo=True)

### Criar a sessão assíncrona
AsyncSessionLocal = async_sessionmaker(
    autocommit=False, # não faz o commit automaticamente
    autoflush=False,  # não faz o flush automaticamente
    # Commit + Flush = Salvar 
    bind=engine, 
    class_=AsyncSession
)

async def get_db_session():
    ### Função para injetar a sessão do banco de dados nas rotas do FastAPI
    ### É um generator que garante a sessão fechada corretamente.
    ### Evita problemas de corromper arquivos, banco de dados e performance

    async with AsyncSessionLocal() as session:
        # inicialização da sessão
        print("Antes de abrir a conexão com o banco de dados")
        # conecta com o banco de dados
        yield session
        # finalização da sessão
        print("Depois de fechar a conexão com o banco de dados")

        