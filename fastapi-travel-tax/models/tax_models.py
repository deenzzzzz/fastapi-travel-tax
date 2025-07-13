# ...existing code...
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

class Province(Base):
    __tablename__ = "provinces"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    is_secondary = Column(Boolean, default=False)

class TaxReduction(Base):
    __tablename__ = "tax_reductions"
    id = Column(Integer, primary_key=True, index=True)
    province_id = Column(Integer)
    amount = Column(Integer)
# ...existing code...
