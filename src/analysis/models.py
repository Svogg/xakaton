from sqlalchemy import Column, ForeignKey, Integer, String, Float, ARRAY, Boolean

from src.database import Base


class _AbstractModel(object):
    id = Column(String, primary_key=True)


class _CityAbstractModel(object):
    city_id = Column(String, ForeignKey('city.id'), nullable=True)


class _GeoAbstractModel(_AbstractModel):
    geo_data = Column(ARRAY(Float), nullable=True)


class _EventsAbstractModel(_CityAbstractModel):
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    duration = Column(String, nullable=False)
    price = Column(Float, nullable=True)


class CityModel(_GeoAbstractModel, Base):
    __tablename__ = 'city'
    city_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    timezone = Column(String, nullable=True)


class AirPlaneTicketModel(_CityAbstractModel, _GeoAbstractModel, Base):
    __tablename__ = 'airplane_ticket'
    target_city = Column(String, ForeignKey('city.id'), nullable=False)
    flight_start = Column(String, nullable=False)
    flight_end = Column(String, nullable=False)
    flight_price = Column(Float, nullable=False)
    airline_name = Column(String, nullable=False)


class EventModel(_AbstractModel, _EventsAbstractModel, Base):
    __tablename__ = 'event'


class ExcursionModel(_AbstractModel, _EventsAbstractModel, Base):
    __tablename__ = 'excursion'


class RestaurantModel(_GeoAbstractModel, _CityAbstractModel, Base):
    __tablename__ = 'restaurant'
    name = Column(String, nullable=True)
    kitchen_type = Column(ARRAY(String), nullable=True)
    mean_price = Column(Float, nullable=True)


class RegionModel(_AbstractModel, Base):
    __tablename__ = 'region'
    title = Column(String, nullable=True)
    price_hotel = Column(Integer, nullable=True)


class HotelModel(_AbstractModel, Base, _CityAbstractModel):
    __tablename__ = 'hotel'
    address = Column(String, nullable=True)
    stars = Column(String, nullable=True)
    geo_data = Column(ARRAY(Float), nullable=True)
    title = Column(String, nullable=True)
    list_services = Column(ARRAY(String), nullable=True)


class UserModel(_AbstractModel, Base):
    __tablename__ = 'user'
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)


class UserAnalyticsModel(Base):
    __tablename__ = 'analytics'
    session = Column(Integer, primary_key=True)
    user_id = Column(String, ForeignKey('user.id'), nullable=True)
    target_region = Column(String, ForeignKey('region.id'), nullable=True)
    current_city = Column(String, ForeignKey('city.id'), nullable=True)
    target_city = Column(String, ForeignKey('city.id'), nullable=True)
    airplane_ticket_to = Column(String, ForeignKey('airplane_ticket.id'), nullable=True)
    airplane_ticket_back = Column(String, ForeignKey('airplane_ticket.id'), nullable=True)
    target_hotel = Column(String, ForeignKey('hotel.id'), nullable=True)
    target_restaurant = Column(String, ForeignKey('restaurant.id'), nullable=True)
    target_excursion = Column(String, ForeignKey('excursion.id'), nullable=True)
    bought = Column(Boolean, nullable=False)

