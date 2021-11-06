import sqlite3


connection = sqlite3.connect("todo.db")


def create_table(connection):
    try:
        cur = connection.cursor()
        cur.execute("""CREATE TABLE task(task text)""")
    except:
        pass


def add_task(connection):
    print("Adding new task!")
    task = input("Name: ")
    if task == "0":
        print("Back to main menu")
    else:
        cur = connection.cursor()
        cur.execute("""INSERT INTO task(task) VALUES(?)""", (task,))
        connection.commit()
        print("Task added successfully!")


def show_tasks(connection):
    print('show tasks in progress')
    cur = connection.cursor()
    cur.execute("""SELECT rowid, task FROM task""")
    result = cur.fetchall()

    for row in result:
        print(str(row[0]) + " - " + row[1])


def delete_task(connection):
    task_index = int(input("Enter index of the task to delete: "))
    cur = connection.cursor()
    rows_deleted = cur.execute("""DELETE FROM task WHERE rowid=?""", (task_index,)).rowcount
    connection.commit()
    if rows_deleted == 0:
        print("Error when deleting. Try again later.")
    else:
        print("Task removed successfully!")


#################################################################################
#################################################################################


create_table(connection)


while True:

    print("\n1. Add task")
    print("2. Show tasks")
    print("3. Remove task")
    print("4. Exit")

    user_choice = int(input("Choose an option: "))

    if user_choice == 1:
        add_task(connection)

    if user_choice == 2:
        show_tasks(connection)

    if user_choice == 3:
        delete_task(connection)

    if user_choice == 4:
        break

    if user_choice < 1 or user_choice > 5:
        print("Enter a number from 1 to 5!")

#################################################################################
#################################################################################

connection.close()
