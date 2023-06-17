from models import User as SAuser, Task
from session import session


class UserRepository:
    def email_check(self, login):
        user = session.query(SAuser).filter_by(email=login).one_or_none()
        if user:
            return user.id
        else:
            return False

    def password_check(self, password):
        user = session.query(SAuser).filter_by(email=login).one()
        if password == user.password:
            self.passw = True
        else:
            self.passw = False
        return self.passw

    # turi tikrinti ir emaila ir passworda iskart

    def register_user(self, login, name, surname, password):
        new_user = SAuser(name=name, surname=surname, email=login, password=password)
        session.add(new_user)
        session.commit()


class TaskRepository:
    def add_task(self, user_id):
        task = Task(title, description, deadline, user_id)
        session.add(task)
        session.commit()

    def update_task(self, change_id):
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
            if change == 4:
                break
        session.commit()

    def delete_task(self, delete_id):
        task_delete = session.query(Task).get(delete_id)
        session.delete(task_delete)
        session.commit()

    def show_tasks(self):
        # retrieve User tasks from the database
        tasks = session.query(Task).filter_by(user_id=user_id).all()
        for task in tasks:
            print(task)


# CLI /////

print("Welcome TO DO list application")
print("To start work with tasks You need to log in")

user_repo = UserRepository()

login = input("Please enter email:")

user_id = user_repo.email_check(login)

if user_repo.email_check(login) == False:
    print("Please register new user")
    name = input("Enter name ")
    surname = input("Enter surname ")
    password = input("Enter password ")
    user_repo.register_user(login, name, surname, password)

else:
    print("User email exists in users table")


password = input("Please enter password:")
if user_repo.password_check(password):
    print("Please manage Your tasks")
else:
    user_repo.password_check(password)
    print("Your password is wrong. Please enter right password")

task_repo = TaskRepository()

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
        task_repo.add_task(user_id)

    if choose == 2:
        task_repo.show_tasks()
        change_id = int(input("Please enter change task id:"))
        task_repo.update_task(change_id)

    if choose == 3:
        task_repo.show_tasks()
        delete_id = int(input("Please enter delete task id:"))
        task_repo.delete_task(delete_id)

    if choose == 4:
        task_repo.show_tasks()

    if choose == 5:
        print("Thank You for using ToDolist app. You exit!")
        break
