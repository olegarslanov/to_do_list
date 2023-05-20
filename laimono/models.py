from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    password = Column("Password", String)
    data = relationship("Data", back_populates="user")

    def __repr__(self):
        return f"{self.name}, {self.surname},  {self.email}"


class Data(Base):
    __tablename__ = "data"
    id = Column(Integer, primary_key=True)
    type = Column("Type", String)
    attribute = Column("Attribute", String)
    attribute2 = Column("Attribute 2", String)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="data")

    def __repr__(self):
        return f"{self.type} -- {self.attribute},  {self.attribute2}"
