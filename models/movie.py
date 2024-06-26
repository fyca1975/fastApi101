from config.database import Base 
from sqlalchemy import Column, Float, Integer, String


class Movie(Base):

    __tablename__ = "movies"

    id = Column(Integer, primary_key= True)
    tittle = Column(String)
    overview = Column(String)
    year = Column(Integer)
    rating = Column(Float)
    category = Column(String)
