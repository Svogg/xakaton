from sqlalchemy import (
    Column, ForeignKey, Integer, String, Float, ARRAY
)

from ..database import Base, engine



class _AbstractModel(object):
    id = Column(String, primary_key=True)


class _CityAbstractModel(object):
    city_id = Column(String, ForeignKey('city.id'), nullable=True)


class _GeoAbstractModel(_AbstractModel):
    geo_data = Column(ARRAY(Float), nullable=True)


class _EventsAbstractModel(_CityAbstractModel):
    start = Column(String, nullable=False)
    end = Column(String, nullable=False)
    price = Column(Float, nullable=True)


class CityModel(_GeoAbstractModel, Base):
    __tablename__ = 'city'
    city_name = Column(String, nullable=False)
    rating = Column(Integer, nullable=True)
    timezone = Column(String, nullable=True)


class EventModel(_AbstractModel, _EventsAbstractModel, Base):
    __tablename__ = 'event'


class ExcursionModel(_AbstractModel, _EventsAbstractModel, Base):
    __tablename__ = 'excursion'


class RestaurantModel(_GeoAbstractModel, _CityAbstractModel, Base):
    __tablename__ = 'restaurant'
    name = Column(String, nullable=True)
    kitchen_type = Column(ARRAY(String), nullable=True)
    mean_price = Column(Float, nullable=True)


class TrackModel(_AbstractModel, Base, _CityAbstractModel):
    __tablename__ = 'track'
    region = Column(String, ForeignKey('region.id'))
    days_count = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=True)


class RegionModel(_AbstractModel, Base):
    __tablename__ = 'region'
    title = Column(String, nullable=True)
    price_hotel = Column(Integer, nullable=True)


class RouteModel(_AbstractModel, Base, _CityAbstractModel):
    __tablename__ = 'route'
    title = Column(String, nullable=True)
    time = Column(String, nullable=True)


class HotelModel(_AbstractModel, Base, _CityAbstractModel):
    __tablename__ = 'hotel'
    address = Column(String, nullable=True)
    geo_data = Column(ARRAY(Float), nullable=True)
    title = Column(String, nullable=True)


class UserAnalyticsModel(Base):
    __tablename__ = 'analytics'
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(String, ForeignKey('user.id'))
    key = Column(String, nullable=False)
    time = Column(Integer, nullable=False)


class UserModel(Base):
    __tablename__ = 'user'
    id = Column(String, primary_key=True)
    email = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
