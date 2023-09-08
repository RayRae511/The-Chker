import sqlite3
import datetime
import fire

conn = sqlite3.connect("expenses.db")
cur = conn.cursor()

while True:
    print("Select an option:")
    print("1. Enter a new expense")
    print("2. View expenses summary")

    choice = int(input())

    if choice == 1:
        date = input("Enter the date of expense (YYYY-MM-DD): ")
        description = input("Enter description of expense: ")

        cur.execute("SELECT DISTINCT category FROM expenses")
        categories = cur.fetchall()

        print("Select category by number:")
        for index, category in enumerate(categories):
            print(f"{index + 1}. {category[0]}")
        print(f"{len(categories) + 1}. Create a category")

        category_choice = input("Enter the category number: ")
        category_choice = int(category_choice)

        if 1 <= category_choice <= len(categories):
            category = categories[category_choice - 1][0]
        elif category_choice == len(categories) + 1:
            new_category = input("Enter the name of the new category: ")
            cur.execute("INSERT INTO expenses (category) VALUES (?)", (new_category,))
            conn.commit()
            category = new_category
        else:
            print("Invalid category number. Please select a valid category.")
            continue

        price = float(input("Enter the price of expense: "))
        cur.execute("INSERT INTO expenses (Date, description, category, price) VALUES (?, ?, ?, ?)",
                    (date, description, category, price))
        conn.commit()

    elif choice == 2:
        print("Select option:")
        print("1. View all expenses")
        print("2. View monthly expenses by category")

        view_choice = int(input())
        if view_choice == 1:
            cur.execute("SELECT * FROM expenses")
            expenses = cur.fetchall()
            for expense in expenses:
                print(expense)

        elif view_choice == 2:
            month = input("Enter the month (MM): ")
            year = input("Enter the year (YYYY): ")
            cur.execute("""SELECT category, SUM(price) FROM expenses 
                           WHERE strftime("%m", Date) = ? AND strftime('%Y', Date) = ?
                           GROUP BY category""", (month, year))
            expenses = cur.fetchall()
            for expense in expenses:
                print(f"Category: {expense[0]}, Total: {expense[1]}")
        else:
            exit()

    else:
        exit()

    repeat = input("Would you like to do something else (Yes/No)?\n")
    if repeat.lower() != "yes":
        break

conn.close()