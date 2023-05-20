from app_new import Application
from database import SqliteDatabase

run = Application(SqliteDatabase("user_data.db"))
run.run()
