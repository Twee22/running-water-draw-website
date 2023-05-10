"""Add new columns to Vendor model

Revision ID: 9c54ffdf8b55
Revises: e389157bc8f9
Create Date: 2023-05-10 15:30:45.060764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c54ffdf8b55'
down_revision = 'e389157bc8f9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_text', schema=None) as batch_op:
        batch_op.add_column(sa.Column('festival', sa.String(), server_default="The Plainview Rotary Club's 49th Annual Running Water Draw Festival will be held at the Ollie Liner Center (2000 S. Columbia St.) on Friday, Saturday and Sunday, October 20th, 21st & 22nd.", nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('app_text', schema=None) as batch_op:
        batch_op.drop_column('festival')

    # ### end Alembic commands ###
