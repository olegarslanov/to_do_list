from main_sugadintas import UserRepository, TaskRepository

# User interface
print("Welcome TO DO list application")
print("To start work with tasks You need to log in")
user = UserRepository()
login = input("Please enter email:")
user.email_check(login)

print("User email exists in users table")

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
