"""empty message

Revision ID: 4c963476f9b4
Revises: 00430cb1bf62
Create Date: 2022-10-14 17:44:15.493742

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c963476f9b4'
down_revision = '00430cb1bf62'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('description', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('items', 'description')
    # ### end Alembic commands ###
