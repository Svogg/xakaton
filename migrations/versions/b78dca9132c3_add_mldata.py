"""add mldata

Revision ID: b78dca9132c3
Revises: 
Create Date: 2023-05-27 12:46:58.061676

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b78dca9132c3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mldata',
    sa.Column('pk', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item_id', sa.String(), nullable=True),
    sa.Column('user_id', sa.String(), nullable=True),
    sa.Column('bought', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('pk')
    )
    op.create_table('airplane_ticket',
    sa.Column('target_city', sa.String(), nullable=False),
    sa.Column('flight_start', sa.String(), nullable=False),
    sa.Column('flight_end', sa.String(), nullable=False),
    sa.Column('flight_price', sa.Float(), nullable=False),
    sa.Column('airline_name', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['target_city'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('track')
    op.drop_table('route')
    op.add_column('analytics', sa.Column('session', sa.Integer(), nullable=False))
    op.add_column('analytics', sa.Column('target_region', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('current_city', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('target_city', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('airplane_ticket_to', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('airplane_ticket_back', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('target_hotel', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('target_restaurant', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('target_excursion', sa.String(), nullable=True))
    op.add_column('analytics', sa.Column('bought', sa.Boolean(), nullable=False))
    op.create_foreign_key(None, 'analytics', 'restaurant', ['target_restaurant'], ['id'])
    op.create_foreign_key(None, 'analytics', 'city', ['target_city'], ['id'])
    op.create_foreign_key(None, 'analytics', 'hotel', ['target_hotel'], ['id'])
    op.create_foreign_key(None, 'analytics', 'excursion', ['target_excursion'], ['id'])
    op.create_foreign_key(None, 'analytics', 'airplane_ticket', ['airplane_ticket_to'], ['id'])
    op.create_foreign_key(None, 'analytics', 'city', ['current_city'], ['id'])
    op.create_foreign_key(None, 'analytics', 'region', ['target_region'], ['id'])
    op.create_foreign_key(None, 'analytics', 'airplane_ticket', ['airplane_ticket_back'], ['id'])
    op.drop_column('analytics', 'id')
    op.drop_column('analytics', 'time')
    op.drop_column('analytics', 'key')
    op.add_column('event', sa.Column('duration', sa.String(), nullable=True))
    op.add_column('event', sa.Column('bought_count', sa.Integer(), nullable=True))
    op.alter_column('event', 'start',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('event', 'end',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('excursion', sa.Column('duration', sa.String(), nullable=True))
    op.add_column('excursion', sa.Column('bought_count', sa.Integer(), nullable=True))
    op.alter_column('excursion', 'start',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('excursion', 'end',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.add_column('hotel', sa.Column('stars', sa.String(), nullable=True))
    op.add_column('hotel', sa.Column('list_services', sa.ARRAY(sa.String()), nullable=True))
    op.add_column('hotel', sa.Column('bought_count', sa.Integer(), nullable=True))
    op.add_column('restaurant', sa.Column('bought_count', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('restaurant', 'bought_count')
    op.drop_column('hotel', 'bought_count')
    op.drop_column('hotel', 'list_services')
    op.drop_column('hotel', 'stars')
    op.alter_column('excursion', 'end',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('excursion', 'start',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('excursion', 'bought_count')
    op.drop_column('excursion', 'duration')
    op.alter_column('event', 'end',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('event', 'start',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_column('event', 'bought_count')
    op.drop_column('event', 'duration')
    op.add_column('analytics', sa.Column('key', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.add_column('analytics', sa.Column('time', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('analytics', sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False))
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_constraint(None, 'analytics', type_='foreignkey')
    op.drop_column('analytics', 'bought')
    op.drop_column('analytics', 'target_excursion')
    op.drop_column('analytics', 'target_restaurant')
    op.drop_column('analytics', 'target_hotel')
    op.drop_column('analytics', 'airplane_ticket_back')
    op.drop_column('analytics', 'airplane_ticket_to')
    op.drop_column('analytics', 'target_city')
    op.drop_column('analytics', 'current_city')
    op.drop_column('analytics', 'target_region')
    op.drop_column('analytics', 'session')
    op.create_table('route',
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('time', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], name='route_city_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='route_pkey')
    )
    op.create_table('track',
    sa.Column('region', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('days_count', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('price', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city_id', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], name='track_city_id_fkey'),
    sa.ForeignKeyConstraint(['region'], ['region.id'], name='track_region_fkey'),
    sa.PrimaryKeyConstraint('id', name='track_pkey')
    )
    op.drop_table('airplane_ticket')
    op.drop_table('mldata')
    # ### end Alembic commands ###
