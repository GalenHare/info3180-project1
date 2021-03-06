"""empty message

Revision ID: d37a8b2e39f1
Revises: c79ee7490655
Create Date: 2019-03-18 23:12:51.979524

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd37a8b2e39f1'
down_revision = 'c79ee7490655'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_profiles', sa.Column('date', sa.String(length=80), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user_profiles', 'date')
    # ### end Alembic commands ###
