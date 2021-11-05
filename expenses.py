expenses = []

#################################################################################


def show_stats(month):
    total_amount_this_month = sum(expense_amount for expense_amount, _, expense_month in expenses if expense_month == month)
    number_of_expenses_this_month = sum(1 for _, _, expense_month in expenses if expense_month == month)
    avarage_expense_this_month = total_amount_this_month / number_of_expenses_this_month

    total_amount_all = sum(expense_amount for expense_amount, _, _ in expenses)
    avarage_expense_all = total_amount_all / len(expenses)

    print("\nStatistics")
    print("Total amount this month [pln]:", total_amount_this_month)
    print("Avarage:", avarage_expense_this_month)
    print("Total amount all-time [pln]:", total_amount_all)
    print("Avarage (all):", avarage_expense_all)


def show_expenses(month):
    for expense_amount, expense_type, expense_month in expenses:
        if expense_month == month:
            print(f'{expense_amount} - {expense_type}')


def add_expense(month):
    print()
    expense_amount = int(input("How much money did you spent [pln]: "))
    expense_type = input("What type of expense [food, clothes, different]: ")

    expense = (expense_amount, expense_type, month)
    expenses.append(expense)


#################################################################################
#################################################################################


while True:
    print()
    month = int(input("Month [1-12]: "))

    if month == 0:
        break

    while True:
        print("\n0. Back to main menu")
        print("1. Show all expenses")
        print("2. Add new expense")
        print("3. Statistics")
        choice = int(input("Choose an option: "))

        if choice == 0:
            break

        if choice == 1:
            show_expenses(month)

        if choice == 2:
            add_expense(month)

        if choice == 3:
            show_stats(month)
