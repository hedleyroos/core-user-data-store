"""empty message

Revision ID: 4a3f1279bc80
Revises: 90c7632a894b
Create Date: 2018-05-16 07:44:46.759720

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '4a3f1279bc80'
down_revision = '90c7632a894b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usersitedata', 'blocked')
    op.drop_column('usersitedata', 'consented_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('usersitedata', sa.Column('consented_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('usersitedata', sa.Column('blocked', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###