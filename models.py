from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, create_engine, MetaData, LargeBinary, Float
from sqlalchemy.types import UserDefinedType
from geoalchemy2 import Geometry, Geography
from sqlalchemy.orm import relationship, DeclarativeBase
from config import DB_DRIVER, DB_CONNECTOR, DB_USER, DB_PASS, DB_HOST, DB_PORT, DB_NAME

DATABASE_URL = "{}+{}://{}:{}@{}:{}/{}".format(
    DB_DRIVER, DB_CONNECTOR,
    DB_USER, DB_PASS,
    DB_HOST, DB_PORT,
    DB_NAME
)

metadata = MetaData()

engine = create_engine(
    DATABASE_URL
)


class Abstract(object):
    id = Column(String, primary_key=True)


class Base(DeclarativeBase):
    pass


class Country(Abstract, Base):
    __tablename__ = 'country'
    country_name = Column(String, nullable=False)
    region = Column(String, nullable=False)
    coat_of_arms = Column(String, nullable=False)
    alias_name = Column(String, nullable=False)


class Icon(Abstract, Base):
    __tablename__ = 'icon'
    binary_icon = Column(LargeBinary, nullable=False)


class HPImage(Abstract, Base):
    __tablename__ = 'hp_image'
    binary_hp_image = Column(LargeBinary, nullable=False)


class Image(Abstract, Base):
    __tablename__ = 'image'
    binary_image = Column(LargeBinary, nullable=False)


class CityGuide(Abstract, Base):
    __tablename__ = 'city_guide'
    cg_image = Column(LargeBinary, nullable=False)


class Gallery(Abstract, Base):
    __tablename__ = 'gallery'
    gallery_image = Column(LargeBinary, nullable=False)


class GeoData(Abstract, Base):
    __tablename__ = 'geo_data'
    center_distance = Column(Float)
    coordinates_length = Column(Float, nullable=False)
    coordinates_width = Column(Float, nullable=False)
    # om_map = Column(Geometry(geometry_type='POINT', srid=4326), nullable=False)
    type = Column(String, nullable=False)


class Day(Abstract, Base):
    __tablename__ = 'day'
    day_name = Column(String, unique=True, nullable=False)


class WorkingTime(Abstract, Base):
    __tablename__ = 'working_time'
    day_id = Column(String, ForeignKey('day.id'))
    closed = Column(Boolean)


class GooglePlace(Abstract, Base):
    __tablename__ = 'google_place'
    use_manual_schedule = Column(Boolean)


class City(Abstract, Base):
    __tablename__ = 'city'
    city_name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    description_title = Column(String, nullable=False)
    external_id = Column(String, nullable=False)
    import_dined = Column(Boolean)
    is_priority = Column(Boolean)
    rating = Column(Integer, nullable=False)
    short_description = Column(String)
    sort = Column(Integer, nullable=False)
    timezone = Column(String, nullable=False)
    title = Column(String, nullable=False)
    title_dative = Column(String, nullable=False)
    title_genitive = Column(String, nullable=False)
    travel_line_id = Column(String, nullable=False)
    weather_sync = Column(Boolean)
    ya_id = Column(String, nullable=False)

    country_id = Column(String, ForeignKey('country.id'))
    icon_id = Column(String, ForeignKey('icon.id'))
    image_id = Column(String, ForeignKey('image.id'))
    city_guide_id = Column(String, ForeignKey('city_guide.id'))
    cg_image_id = Column(String, ForeignKey('city_guide.id'))
    hp_image_id = Column(String, ForeignKey('hp_image.id'))
    gallery_id = Column(String, ForeignKey('gallery.id'))
    geo_data_id = Column(String, ForeignKey('geo_data.id'))
    working_time = Column(String, ForeignKey('working_time.id'))
    google_place_id = Column(String, ForeignKey('google_place.id'))


Base.metadata.create_all(engine)
