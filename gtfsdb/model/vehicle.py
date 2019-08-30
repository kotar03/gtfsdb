from sqlalchemy import Column, Sequence
from sqlalchemy.types import Integer, String

from gtfsdb import config
from gtfsdb.model.base import Base


class Agency(Base):
    datasource = config.DATASOURCE_DERIVED
    __tablename__ = 'vehicles'

    id = Column(Integer, Sequence(None, optional=True), primary_key=True, nullable=True)
    agency_id = Column(String(255), index=True, unique=True)