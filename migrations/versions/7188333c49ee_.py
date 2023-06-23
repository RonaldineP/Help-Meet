"""empty message

Revision ID: 7188333c49ee
Revises: 227b8756616a
Create Date: 2023-06-19 22:22:52.827914

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7188333c49ee'
down_revision = '227b8756616a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=256),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('location',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)
        batch_op.alter_column('city',
               existing_type=sa.VARCHAR(length=256),
               nullable=True)

    # ### end Alembic commands ###
