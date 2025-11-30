from ..config import Base
from sqlalchemy import Integer, Column, String, Text


class Article(Base):

    __tablename__ = "article"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    body = Column(Text)
