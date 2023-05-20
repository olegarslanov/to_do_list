from models import User as SAuser, Task
from session import session


class UserRepository:
    def email_check(self, login):
        return session.query(SAuser).filter_by(email=login).first()

    def password_check(self, password):
        user = session.query(SAuser).filter_by(email=login).one()
        if password == user.password:
            self.passw = True
        else:
            self.passw = False
        return self.passw

    def register_user(self, login):
        new_user = SAuser(name=name, surname=surname, email=login, password=password)
        session.add(new_user)
        session.commit()
        exit()


class TaskRepository:
    def add_task(self, user):
        task = Task(
            title=title, description=description, deadline=deadline, user_id=user.id
        )
        session.add(task)
        session.commit()

    def update_task(self, change_id):
        task = session.query(Task).get(change_id)
        task.title = new_title
        task.description = new_description
        task.deadline = new_deadline
        session.commit()

    def delete_task(self, delete_id):
        task_delete = session.query(Task).get(delete_id)
        session.delete(task_delete)
        session.commit()

    def show_tasks(self):
        # retrieve User tasks from the database
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)


# User interface /////

print("Welcome TO DO list application")
print("To start work with tasks You need to log in")

user = UserRepository()
login = input("Please enter email:")
user.email_check(login)

if user.email_check(login) is None:
    print("User not found. Please register new user")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    password = input("Enter password: ")
    user.register_user(login)

    print("User email exists in users table")

password = input("Please enter password:")
user.password_check(password)

if user.passw == 1:
    print("Now You can manage Your tasks")

if user.passw == 0:
    print("Password is not correct")
    exit()


task = TaskRepository()

while True:
    choose = int(
        input(
            "Please enter Your choice: \n1 - create task \n2 - update task \n3 - delete task \n4 - show all Your tasks \n5 - exit app\n"
        )
    )
    if choose == 1:
        title = input("Please input title:")
        description = input("Please input description:")
        deadline = input("Please input deadline:")
        task.add_task()

    if choose == 2:
        # task.show_tasks()

        change_id = int(input("Please enter change task id:"))
        while True:
            change = int(
                input(
                    "Enter change: \n 1 - title, \n 2 - description, \n 3 - deadline :\n 4 - exit update task \n "
                )
            )
            if change == 1:
                new_title = input("Please enter task title:")
            if change == 2:
                new_description = input("Please enter task description:")
            if change == 3:
                new_deadline = input("Please enter task deadline:")
            if change == 4:
                break

        task.update_task(change_id)

    if choose == 3:
        task.show_tasks()
        delete_id = int(input("Please enter delete task id:"))
        task.delete_task(delete_id)

    if choose == 4:
        task.show_tasks()

    if choose == 5:
        print("Thank You for using ToDolist app. You exit!")
        break
