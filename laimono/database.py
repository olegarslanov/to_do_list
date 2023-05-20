from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import User, Data, Base


class SqliteDatabase:
    def __init__(self, filename: str) -> None:
        self.filename = filename
        self.base = Base
        self.engine = create_engine(f"sqlite:///{self.filename}")
        self.session = sessionmaker(bind=self.engine)

    def create_database(self):
        self.base.metadata.create_all(self.engine)

    def create_user(self, **kwargs):
        try:
            object = User(**kwargs)
            session = self.session()
            session.add(object)
            session.commit()
            return None
        except Exception as exception:
            session.rollback()
            return f"Something went wrong: {exception}"

    def create_data(self, **kwargs):
        try:
            object = Data(**kwargs)
            session = self.session()
            session.add(object)
            session.commit()
            return None
        except Exception as exception:
            session.rollback()
            return f"Something went wrong: {exception}"

    def get_user(self, userid):
        try:
            session = self.session()
            got_user = session.query(User).filter(User.id == userid).one()
            return got_user
        except Exception as exception:
            session.rollback()
            return f"Something went wrong: {exception}"

    def get_data(self, userid):
        session = self.session()
        got_data = session.query(User).filter(User.id == userid).one()
        data = got_data.data
        return data

    def update_data(self, userid, dataid, field, value):
        session = self.session()
        user = session.query(User).get(userid)
        data = user.data[dataid]
        attr_name = field
        attr_value = value
        setattr(data, attr_name, attr_value)
        session.commit()

    def delete_data(self, userid, dataid):
        session = self.session()
        user = session.query(User).get(userid)
        data = user.data[dataid]
        session.delete(data)
        session.commit()

    def get_users(self):
        session = self.session()
        users = session.query(User).all()
        return users

    def get_user_by_email(self, login: str):
        session = self.session()
        user = session.query(User).filter(User.email == login).first()
        return user
