# Expense Tracker in Python

expenses = []

def add_expense():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")
    amount = float(input("Enter amount: "))
    expenses.append({"date": date, "description": description, "amount": amount})
    print("Expense added!\n")

def view_expenses():
    print("\nExpenses:")
    for expense in expenses:
        print(f"Date: {expense['date']}, Description: {expense['description']}, Amount: {expense['amount']}")
    print("")

def delete_expense():
    description = input("Enter description of the expense to delete: ")
    for expense in expenses:
        if expense['description'] == description:
            expenses.remove(expense)
            print("Expense deleted!\n")
            return
    print("Expense not found!\n")

def main():
    while True:
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            delete_expense()
        elif choice == "4":
            break
        else:
            print("Invalid choice!")

main()
