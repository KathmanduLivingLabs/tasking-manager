"""empty message

Revision ID: 824268a7a675
Revises: 30b091260689
Create Date: 2018-12-07 12:54:19.964101

"""
from alembic import op


# revision identifiers, used by Alembic.
revision = "824268a7a675"
down_revision = "30b091260689"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("tasks", "splittable", new_column_name="is_square")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("tasks", "is_square", new_column_name="splittable")
    # ### end Alembic commands ###
