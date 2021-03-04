"""empty message

Revision ID: 3d40b59d3175
Revises: 
Create Date: 2021-03-04 16:34:09.230975

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d40b59d3175'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=60), nullable=True),
    sa.Column('lastname', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('profilePicture', sa.String(length=300), nullable=True),
    sa.Column('dataOfRegister', sa.Date(), nullable=True),
    sa.Column('accountType', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###