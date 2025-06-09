"""adiciona coluna cpf na tabela autor

Revision ID: abc123def456
Revises: 9fb870f94da5
Create Date: 2025-06-08 16:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = 'abc123def456'         
down_revision = '9fb870f94da5'   
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('autor', sa.Column('cpf', sa.String(), unique=True, index=True, nullable=True))


def downgrade():
    op.drop_column('autor', 'cpf')
