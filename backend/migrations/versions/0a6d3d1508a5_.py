"""empty message

Revision ID: 0a6d3d1508a5
Revises: 3d40b59d3175
Create Date: 2021-03-04 16:52:27.728243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a6d3d1508a5'
down_revision = '3d40b59d3175'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=60), nullable=True),
    sa.Column('lastname', sa.String(length=60), nullable=True),
    sa.Column('email', sa.String(length=60), nullable=True),
    sa.Column('password', sa.String(length=60), nullable=True),
    sa.Column('profilePicture', sa.String(length=300), nullable=True),
    sa.Column('dataOfRegister', sa.Date(), nullable=True),
    sa.Column('designation', sa.String(length=60), nullable=True),
    sa.Column('lng', sa.String(length=60), nullable=True),
    sa.Column('lat', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('admin')
    # ### end Alembic commands ###
