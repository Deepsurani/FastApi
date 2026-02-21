from sqlalchemy import Column,Integer,String
from .database import Base

class Student(Base):

    __tablename__ = "students"

    id = Column(Integer,primary_key=True,index=True)
    Name = Column(String(100))
    Email = Column(String(100))
    Age = Column(Integer)
