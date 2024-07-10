"""'Added'

Revision ID: 9101005272d8
Revises: 0d997d1ee9c2
Create Date: 2024-07-08 11:11:30.544139

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9101005272d8'
down_revision = '0d997d1ee9c2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('poster_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key('fk_posts_poster_id', 'users', ['poster_id'], ['id'])
        batch_op.drop_column('author')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('posts', schema=None) as batch_op:
        batch_op.add_column(sa.Column('author', sa.VARCHAR(length=255), nullable=True))
        batch_op.drop_constraint('fk_posts_poster_id', type_='foreignkey')
        batch_op.drop_column('poster_id')

    # ### end Alembic commands ###
