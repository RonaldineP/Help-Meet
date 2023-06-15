"""empty message

Revision ID: f3eb9fd5df59
Revises: 
Create Date: 2023-06-15 19:00:57.623870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f3eb9fd5df59'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=256), nullable=False),
    sa.Column('profile_image', sa.String(length=256), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('name', sa.String(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('profile_image')
    )
    op.create_table('helper',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('bio', sa.String(length=500), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=False),
    sa.Column('location', sa.String(length=256), nullable=False),
    sa.Column('date', sa.String(length=256), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('image',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=500), nullable=False),
    sa.Column('public_id', sa.String(length=250), nullable=False),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('public_id')
    )
    op.create_table('post_candidate',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('helper_id', sa.Integer(), nullable=True),
    sa.Column('post_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['helper_id'], ['helper.id'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('post_candidate')
    op.drop_table('image')
    op.drop_table('post')
    op.drop_table('helper')
    op.drop_table('user')
    # ### end Alembic commands ###