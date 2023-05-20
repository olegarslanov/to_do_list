from models import User as SAuser, Task
from session import session


class UserRepository:
    def email_check(self, login):
        user_list = session.query(SAuser).all()
        for user in user_list:
            if user.email == login:
                answer = 1
                break
        else:
            answer = 0
        return answer

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
    def add_task(self):
        self.user_id = user.id
        task = Task(self.title, self.description, self.deadline, self.user_id)
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
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)


# User interface /////

print("Welcome TO DO list application")
print("To start work with tasks You need to log in")

user = UserRepository()
login = input("Please enter email:")
user.email_check(login)

if user.email_check(login) == 0:
    print("Please register new user")
    name = input("Enter name ")
    surname = input("Enter surname ")
    password = input("Enter password ")
    user.register_user(login)

if user.email_check(login) == 1:
    print("User email exists in users table")

password = input("Please enter password:")
user.password_check(password)

if user.passw == False:
    print("Now You can manage Your tasks")
if user.passw == True:
    exit()


task = TaskRepository()

while True:
    choose = int(
        input(
            "Please enter Your choice: \n1 - create task \n2 - update task \n3 - delete task \n4 - show all Your tasks \n5 - exit app\n"
        )
    )
    if choose == 1:
        task.title = input("Please input title:")
        task.description = input("Please input description:")
        task.deadline = input("Please input deadline:")
        task.add_task()

    if choose == 2:
        task.show_tasks()

        change_id = int(input("Please enter change task id:"))
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
