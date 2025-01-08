"""Initial migration

Revision ID: ddf03f4cb989
Revises: 00386817086e
Create Date: 2025-01-08 01:32:05.822191

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = 'ddf03f4cb989'
down_revision: Union[str, None] = '00386817086e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('booking',
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=False),
    sa.Column('uuid', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.Uuid(), nullable=False),
    sa.Column('facility_id', sa.Uuid(), nullable=False),
    sa.Column('procedure_id', sa.Uuid(), nullable=False),
    sa.Column('itinerary', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('status', sa.Enum('PENDING', 'CONFIRMED', 'CANCELLED', 'COMPLETED', name='bookingstatus'), nullable=False),
    sa.ForeignKeyConstraint(['facility_id'], ['facility.uuid'], ),
    sa.ForeignKeyConstraint(['procedure_id'], ['procedure.uuid'], ),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_index(op.f('ix_booking_user_id'), 'booking', ['user_id'], unique=False)
    op.create_index(op.f('ix_booking_uuid'), 'booking', ['uuid'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_booking_uuid'), table_name='booking')
    op.drop_index(op.f('ix_booking_user_id'), table_name='booking')
    op.drop_table('booking')
    # ### end Alembic commands ###
