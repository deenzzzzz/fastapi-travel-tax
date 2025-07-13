# ...existing code...
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi_travel_tax.models.tax_models import Base

DATABASE_URL = "sqlite:///./travel_tax.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create tables
Base.metadata.create_all(bind=engine)
# ...existing code...
