from sqlalchemy import Column, Integer, String, Float
from .database import Base

class Price(Base):
    __tablename__ = "prices"

    id = Column(Integer, primary_key=True)
    product = Column(String)
    price = Column(Float)
    source = Column(String)
