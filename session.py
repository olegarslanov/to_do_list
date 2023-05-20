from sqlalchemy.orm import sessionmaker
from models import engine

# sukuriu klases Session egzemplioriu
Session = sessionmaker(bind=engine)
session = Session()
