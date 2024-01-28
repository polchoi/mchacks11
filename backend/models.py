from sqlalchemy import Column, Integer, String, Float
from database import Base

class Users(Base):
    __tablename__ = "users"
    
    username = Column(String(50), primary_key=True, index=True)
    name = Column(String(50))
    
class ExpenseRecord(Base):
    __tablename__ = "expense_records"
    
    id = Column(Integer, primary_key=True, index=True)
    # username = Column(String(50))
    merchant_name = Column(String(100))
    price = Column(Float)
    category = Column(String(50))