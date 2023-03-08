import mysql.connector
import sqlalchemy
from sqlalchemy.orm import DeclarativeBase

engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/dbtestowa',echo=True)
