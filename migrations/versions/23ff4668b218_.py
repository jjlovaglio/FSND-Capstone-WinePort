"""empty message

Revision ID: 23ff4668b218
Revises: 4be81656bb81
Create Date: 2021-01-21 12:27:42.485020

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '23ff4668b218'
down_revision = '4be81656bb81'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'artist', ['facebook_link'])
    op.create_unique_constraint(None, 'artist', ['name'])
    op.create_unique_constraint(None, 'venue', ['phone'])
    op.create_unique_constraint(None, 'venue', ['name'])
    op.create_unique_constraint(None, 'venue', ['facebook_link'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'venue', type_='unique')
    op.drop_constraint(None, 'venue', type_='unique')
    op.drop_constraint(None, 'venue', type_='unique')
    op.drop_constraint(None, 'artist', type_='unique')
    op.drop_constraint(None, 'artist', type_='unique')
    # ### end Alembic commands ###