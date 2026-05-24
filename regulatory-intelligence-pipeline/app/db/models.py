from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base

class Regulation(Base):
    __tablename__ = "regulations"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    summary = Column(Text)
    risk_level = Column(String)