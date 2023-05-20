from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# sukuriam pajungimas prie duomenu bazes
engine = create_engine("sqlite:///user_tasks.db")
# sukuriu declarative_base klases egzemplioriu (rysiai tarp musu lenteliu)
Base = declarative_base()


# Nutariau naudoti one2many metoda, sukurti lenteliu sablonai


# sukuriam lenteles User modeli
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column("Name", String)
    surname = Column("Surname", String)
    email = Column("Email", String)
    password = Column("Password", String)
    tasks = relationship("Task", back_populates="user")

    # def __init__(self, name, surname, email, password):
    #     self.name = name
    #     self.surname = surname
    #     self.email = email
    #     self.password = password

    def __repr__(self):
        return f"{self.id} {self.name} {self.surname} {self.email} {self.password}"


class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    title = Column("Title", String)
    description = Column("Description", String)
    deadline = Column("Deadline", String)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", back_populates="tasks")

    def __init__(self, title, description, deadline, user_id):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.user_id = user_id

    def __repr__(self):
        return (
            f"{self.id} {self.title} {self.description} {self.deadline} {self.user_id}"
        )


# sukuriu lenteles duomenu bazeje
Base.metadata.create_all(engine)
