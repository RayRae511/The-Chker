import sqlite3
import datetime


conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choise = int(input())

    if choise == 1:
        date = input("Enter the date of expense (YYYY-MM-DD):")
        description = input("Enter description of expense:")

        cur.execute("SELECT DISTINCT category FROM expenses")

        categories = cur.fetchall()
        print("Select category by number:")
        for index, category in enumerate(categories):
            print(f"{index + 1}, {category[0]}")
        print(f"{len(categories) + 1}. Create a category")

        category_choise = input()
        if category_choise == len(categories) + 1:
            category = input("Enter the new name of category:")
        else:
            category = categories[category_choise - 1][0]

        price = input("Enter the price of expense: ")
        cur.execute("INSERT INTO expenses(Date, description, category, price)")
        conn.commit()

    elif choise == 2:
        print("Select option:")
        print("1. View all expenses")
        print("2. View monthly expenses by category")

        view_choise = int(input())
        if view_choise == 1:
            cur.executr("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)

        elif view_choise == 2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            cur.execute("""SELECT category, SUM(price) FROM expenses WHERE strftime("%m", Date) = ? AND strftime('%Y', Date) = ?
                        GROUP BY category""", (month, year))
            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()

    else:
        exit()

    repeat = input("Would you like to do something else (Yes/No)?\n")
    if repeat.lower() != "Yes":
        break

conn.close()