
print("Start small. Ship something.\n")

expense = {}

def addexpense(name, amount):
    expense[name] = amount
    print("Expense added successfully!")

def viewexpense(expense):
    if not expense:
        print("No expenses found.")
        return

    for name, amount in expense.items():
        print(name, ":", amount)

def calculate_total(expense):
    total = sum(expense.values())
    print("Total expenses:", total)

def deleteexpense(keyword, expense):
    if keyword in expense:
        expense.pop(keyword)
        print("Expense deleted successfully!")
    else:
        print("Expense not found!")

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Exit")
    print("5. Delete Expense")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))
        addexpense(name, amount)

    elif choice == "2":
        viewexpense(expense)

    elif choice == "3":
        calculate_total(expense)

    elif choice == "4":
        print("Exiting Expense Tracker...")
        break

    elif choice == "5":
        keyword = input("Enter expense name to delete: ")
        deleteexpense(keyword, expense)

    else:
        print("Invalid choice!")
