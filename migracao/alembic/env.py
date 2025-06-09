import sys
import os
from logging.config import fileConfig

from sqlalchemy import engine_from_config, pool
from alembic import context

# Adiciona o diretório raiz ao sys.path para importar app
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importa os modelos e a URL do banco
from app.models import SQLModel
from app.database import DATABASE_URL

# Carrega a configuração do Alembic
config = context.config

# Configura o logging a partir do arquivo .ini
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# Metadata do SQLModel para autogenerate
target_metadata = SQLModel.metadata

def get_url():
    return DATABASE_URL

def run_migrations_offline():
    """Executa as migrações em modo offline."""
    url = get_url()
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Executa as migrações em modo online."""
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = engine_from_config(
        configuration,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
