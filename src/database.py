from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

from typing import Generator
from sqlalchemy.orm import Session

url_database = 'mysql+pymysql://root:root@localhost:3306/basedb'  # Update as needed
engine = create_engine(url_database)
SessionLocal = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()
