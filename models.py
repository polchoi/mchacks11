from sqlalchemy import Column, Integer, String, Float
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    username = Column(String, primary_key=True, index=True)
    name = Column(String)
    
class ExpenseRecord(Base):
    __tablename__ = "expense_records"
    
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    merchant_name = Column(String)
    price = Column(Float)
    category = Column(String)