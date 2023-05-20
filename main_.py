from models import User as SAuser, Task
from session import session


class UserRepository:
    def email_check(self, login):
        return session.query(SAuser).filter_by(email=login).first()

    def password_check(self, user, password):
        if password == user.password:
            return True
        else:
            return False

    def register_user(self, login, name, surname, password):
        new_user = SAuser(name=name, surname=surname, email=login, password=password)
        session.add(new_user)
        session.commit()
        exit()


class TaskRepository:
    def add_task(self, user):
        title = input("Please input title:")
        description = input("Please input description:")
        deadline = input("Please input deadline:")
        task = Task(
            title=title, description=description, deadline=deadline, user_id=user.id
        )
        session.add(task)
        session.commit()

    def update_task(self, user):
        self.show_tasks(user)
        change_id = int(input("Please enter change task id:"))
        while True:
            change = int(
                input(
                    "Enter change:\n1 - title\n2 - description\n3 - deadline\n4 - exit update task\n"
                )
            )
            if change == 1:
                new_title = input("Please enter task title:")
                session.query(Task).filter_by(id=change_id).update({"title": new_title})
                session.commit()
            elif change == 2:
                new_description = input("Please enter task description:")
                session.query(Task).filter_by(id=change_id).update(
                    {"description": new_description}
                )
                session.commit()
            elif change == 3:
                new_deadline = input("Please enter task deadline:")
                session.query(Task).filter_by(id=change_id).update(
                    {"deadline": new_deadline}
                )
                session.commit()
            elif change == 4:
                break

    def delete_task(self, user):
        self.show_tasks(user)
        delete_id = int(input("Please enter delete task id:"))
        task_delete = session.query(Task).get(delete_id)
        session.delete(task_delete)
        session.commit()

    def show_tasks(self, user):
        tasks = session.query(Task).filter_by(user_id=user.id).all()
        for task in tasks:
            print(task)


# User interface /////

print("Welcome TO DO list application")
print("To start work with tasks, you need to log in")

user_repo = UserRepository()
login = input("Please enter email:")
user = user_repo.email_check(login)

if user is None:
    print("User not found. Please register a new user.")
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    password = input("Enter password: ")
    user_repo.register_user(login, name, surname, password)
    user = user_repo.email_check(login)

print("User email exists in users table")

password = input("Please enter password:")
if user_repo.password_check(user, password):
    print("Now you can manage your tasks")
else:
    exit()

task_repo = TaskRepository()

while True:
    choose = int(
        input(
            "Please enter your choice:\n1 - create task\n2 - update task\n3 - delete task\n4 - show all your tasks\n5 - exit app\n"
        )
    )
    if choose == 1:
        task_repo.add_task(user)
    elif choose == 2:
        task_repo.update_task(user)
    elif choose == 3:
        task_repo.delete_task(user)
    elif choose == 4:
        task_repo.show_tasks(user)
    elif choose == 5:
        print("Thank you for using ToDolist app")
        exit()
