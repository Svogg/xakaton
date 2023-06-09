"""initial

Revision ID: 095828e44ea1
Revises: 
Create Date: 2023-05-28 21:38:18.346886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '095828e44ea1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('city',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('city_name', sa.String(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=True),
    sa.Column('timezone', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mldata',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('item_id', sa.String(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('bought', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('region',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('price_hotel', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('disabled', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('airplane_ticket',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('target_city', sa.String(), nullable=False),
    sa.Column('flight_start', sa.String(), nullable=False),
    sa.Column('flight_end', sa.String(), nullable=False),
    sa.Column('flight_price', sa.Float(), nullable=False),
    sa.Column('airline_name', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.ForeignKeyConstraint(['target_city'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('event',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('start', sa.String(), nullable=True),
    sa.Column('end', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('bought_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('excursion',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('start', sa.String(), nullable=True),
    sa.Column('end', sa.String(), nullable=True),
    sa.Column('duration', sa.String(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('bought_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hotel',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('stars', sa.String(), nullable=True),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('list_services', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('bought_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('restaurant',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('city_id', sa.String(), nullable=True),
    sa.Column('geo_data', sa.ARRAY(sa.Float()), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('kitchen_type', sa.ARRAY(sa.String()), nullable=True),
    sa.Column('mean_price', sa.Float(), nullable=True),
    sa.Column('bought_count', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['city_id'], ['city.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('analytics',
    sa.Column('session', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('target_region', sa.String(), nullable=True),
    sa.Column('current_city', sa.String(), nullable=True),
    sa.Column('target_city', sa.String(), nullable=True),
    sa.Column('airplane_ticket_to', sa.String(), nullable=True),
    sa.Column('airplane_ticket_back', sa.String(), nullable=True),
    sa.Column('target_hotel', sa.String(), nullable=True),
    sa.Column('target_restaurant', sa.String(), nullable=True),
    sa.Column('target_excursion', sa.String(), nullable=True),
    sa.Column('bought', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['airplane_ticket_back'], ['airplane_ticket.id'], ),
    sa.ForeignKeyConstraint(['airplane_ticket_to'], ['airplane_ticket.id'], ),
    sa.ForeignKeyConstraint(['current_city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['target_city'], ['city.id'], ),
    sa.ForeignKeyConstraint(['target_excursion'], ['excursion.id'], ),
    sa.ForeignKeyConstraint(['target_hotel'], ['hotel.id'], ),
    sa.ForeignKeyConstraint(['target_region'], ['region.id'], ),
    sa.ForeignKeyConstraint(['target_restaurant'], ['restaurant.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('session')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('analytics')
    op.drop_table('restaurant')
    op.drop_table('hotel')
    op.drop_table('excursion')
    op.drop_table('event')
    op.drop_table('airplane_ticket')
    op.drop_table('user')
    op.drop_table('region')
    op.drop_table('mldata')
    op.drop_table('city')
    # ### end Alembic commands ###
