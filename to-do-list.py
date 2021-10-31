
user_choice = -1
tasks = []

#################################################################################


class Task:
    def __init__(self, name, progress):
        self.name = name
        self.progress = progress

    def show_task(self):
        print("Name: " + self.name + " Progress: " + self.progress)


#################################################################################


def add_task():
    task_name = input("Name: ")
    task_progress = input("0.Done\n1.In progress\nChoose an option: ")

    temp = Task(task_name, task_progress)
    tasks.append(temp)
    print("Task added successfully!")


def show_tasks():
    print()
    task_index = 0
    for task in tasks:
        print("Index: [" + str(task_index) + "] ")
        task.show_task()
        task_index += 1


def delete_task():
    task_index = int(input("Enter index of the task to delete: "))

    if task_index < 0 or task_index > len(tasks) - 1:
        print("Task with this index does not exist!")
        return
    tasks.pop(task_index)
    print("Task removed successfully!")


def save_tasks_to_file(file_name):
    file = open(file_name, "w")
    for task in tasks:
        file.write(task.name + " " + task.progress + "\n")
    file.close()


def load_tasks_from_file(file_name):
    try:
        file = open(file_name)

        for line in file.readlines():
            full_task = line[:-1]  # removed \n
            task_name = full_task[:-1]
            task_progress = full_task[-1]
            temp_task = Task(task_name, task_progress)
            tasks.append(temp_task)
        file.close()
    except FileNotFoundError:
        return


#################################################################################
#################################################################################


file_name = input("Enter name of the file: ")
load_tasks_from_file(file_name)


while user_choice != 5:

    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Save to the file")
    print("5. Exit")

    user_choice = int(input("Choose an option: "))

    if user_choice == 1:
        add_task()

    if user_choice == 2:
        show_tasks()

    if user_choice == 3:
        delete_task()

    if user_choice == 4:
        save_tasks_to_file(file_name)

    if user_choice < 1 or user_choice > 5:
        print("Enter a number from 1 to 5!")
