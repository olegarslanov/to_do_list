from models import User as SAuser, Task
from session import session


class UserRepository:
    def email_check(self, login):
        user_exists = False
        user_list = session.query(SAuser).all()
        for user in user_list:
            if user.email == login:
                user_exists = True
                print("User email exists in users table")
                self.name = user.name
                self.surname = user.surname
                self.email = user.email
                self.password = user.password
                self.id = user.id
        if user_exists is False:
            print("You are new User, please register")
            self.register_user(login)

    def password_check(self, password):
        user = session.query(SAuser).filter_by(email=self.email).one()
        if password == user.password:
            print("Password correct")
            return True
        else:
            print("Password does not match")
            return False

    def register_user(self, login):
        name = input("Enter name ")
        surname = input("Enter surname ")
        password = input("Enter password ")

        new_user = SAuser(name=name, surname=surname, email=login, password=password)
        session.add(new_user)
        session.commit()
        print("Registered succesfully !")
        exit()


class TaskRepository:
    def add_task(self):
        self.title = input("Please input title:")
        self.description = input("Please input description:")
        self.deadline = input("Please input deadline:")
        self.user_id = user.id

        task = Task(self.title, self.description, self.deadline, self.user_id)
        session.add(task)
        session.commit()

    def update_task(self):
        # retrieve User tasks from the database
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)

        change_id = int(input("Please enter change task id:"))
        task_change = session.query(Task).get(change_id)
        while True:
            change = int(
                input(
                    "Enter change: \n 1 - title, \n 2 - description, \n 3 - deadline :\n 4 - exit update task \n "
                )
            )
            if change == 1:
                task_change.title = input("Please enter task title:")
            if change == 2:
                task_change.description = input("Please enter task description:")
            if change == 3:
                task_change.deadline = input("Please enter task deadline:")
            session.commit()
            if change == 4:
                break

    def delete_task(self):
        # retrieve User tasks from the database
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)

        delete_id = int(input("Please enter delete task id:"))
        task_delete = session.query(Task).get(delete_id)
        session.delete(task_delete)
        session.commit()

    def show_tasks(self):
        # retrieve User tasks from the database
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)


# User interface
print("Welcome TO DO list application")
print("To start work with tasks You need to log in")
user = UserRepository()
login = input("Please enter email:")
user.email_check(login)
password = input("Please enter password:")
user.password_check(password)

print("Now You can manage Your tasks")

task = TaskRepository()

while True:
    choose = int(
        input(
            "Please enter Your choice: \n1 - create task \n2 - update task \n3 - delete task \n4 - show all Your tasks \n5 - exit app\n"
        )
    )
    if choose == 1:
        task.add_task()

    if choose == 2:
        task.update_task()

    if choose == 3:
        task.delete_task()

    if choose == 4:
        task.show_tasks()

    if choose == 5:
        print("Thank You for using ToDolist app. You exit!")
        break
