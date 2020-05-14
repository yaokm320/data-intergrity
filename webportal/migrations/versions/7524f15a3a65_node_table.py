"""node table

Revision ID: 7524f15a3a65
Revises: 6ade201dd8ea
Create Date: 2018-02-14 13:26:42.819241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7524f15a3a65'
down_revision = '6ade201dd8ea'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('multichain_node',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('address', sa.String(length=128), nullable=True),
    sa.Column('connect', sa.Boolean(), nullable=True),
    sa.Column('send', sa.Boolean(), nullable=True),
    sa.Column('receive', sa.Boolean(), nullable=True),
    sa.Column('issue', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_multichain_node_address'), 'multichain_node', ['address'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_multichain_node_address'), table_name='multichain_node')
    op.drop_table('multichain_node')
    # ### end Alembic commands ###
