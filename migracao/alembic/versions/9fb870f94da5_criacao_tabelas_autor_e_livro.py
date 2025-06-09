"""criação tabelas autor e livro

Revision ID: 9fb870f94da5
Revises: 
Create Date: 2025-06-08 15:00:00.000000

"""
from alembic import op
import sqlalchemy as sa

revision = '9fb870f94da5'
down_revision = None
branch_labels = None
depends_on = None

def upgrade():
    op.create_table(
        'autor',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(length=100), nullable=False),
        sa.Column('email', sa.String(), nullable=True, index=True),
    )
    op.create_table(
        'livro',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('titulo', sa.String(length=200), nullable=False),
        sa.Column('ano', sa.Integer, nullable=False),
        sa.Column('autor_id', sa.Integer, sa.ForeignKey('autor.id'), nullable=False),
    )

def downgrade():
    op.drop_table('livro')
    op.drop_table('autor')
