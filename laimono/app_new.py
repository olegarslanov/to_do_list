# from database import SqliteDatabase


class Application:
    def __init__(self, database: str) -> None:
        self.db = database
        self.db.create_database()

    def register_user(self, login):
        name = input("Enter name ")
        surname = input("Enter surname ")
        password = input("Enter password ")
        self.db.create_user(name=name, surname=surname, email=login, password=password)
        print("Registered succesfully, now login to get to Your data!")

    def add_data(self, userid):
        data_type = input("Enter data type ")
        attribute = input("Enter data ")
        attribute2 = input("Enter more data ")
        self.db.create_data(
            type=data_type, attribute=attribute, attribute2=attribute2, user_id=userid
        )
        print("Data added succesfully")

    def get_data(self, userid):
        got_data = self.db.get_data(userid=userid)
        for data in got_data:
            print(data)

    def update_data(self, userid):
        dataid = int(input("Which line do You want to update? "))
        field = input(
            "Which field do You want to update: type, attribute or attribute2 "
        )
        value = input("What value do You want to insert? ")
        self.db.update_data(userid=userid, dataid=dataid, field=field, value=value)

    def delete_data(self, userid):
        dataid = int(input("Which line do You want to delete? "))
        self.db.delete_data(userid=userid, dataid=dataid)

    def get_user_by_email(self, userid):
        user = self.db.get_user_by_email(userid)
        if user:
            return user
        else:
            return None

    def run(self):
        print("Hi please be patient!")

        login = input("Enter Your email ")
        user_exists = False
        user = self.db.get_user_by_email(login)  # pataisyk klaida, kai neranda userio
        if user and user.email == login:
            pass_correct = False
            while pass_correct is False:
                user_password = input("Enter password ")
                if user.password == user_password:
                    print(f"Hi, {user.name}")
                    pass_correct = True
            user_exists = True

        if user_exists is False:
            print("You are new User, please register")
            self.register_user(login)

        if user_exists is True and pass_correct is True:
            print("You can now access Your data")
            while True:
                # current_user = self.db.get_user_by_email(login)
                selection = input(
                    """Type:
                '1' to list Your data, 
                '2' to enter more data, 
                '3' to edit data, 
                '4' to delete line of data.
                Or anything else to exit """
                )
                if selection == "1":
                    self.get_data(userid=user.id)
                elif selection == "2":
                    self.add_data(userid=user.id)
                elif selection == "3":
                    self.update_data(userid=user.id)
                elif selection == "4":
                    self.delete_data(userid=user.id)
                else:
                    print("Be carefull, now You'll have to login again!")
                    break
