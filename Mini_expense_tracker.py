expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        item = input("Enter item: ")
        amount = float(input("Enter amount: "))

        expenses.append({
            "item": item,
            "amount": amount
        })

    elif choice == 2:
        for expense in expenses:
            print(expense["item"], ":", expense["amount"])

    elif choice == 3:
        total = sum(expense["amount"] for expense in expenses)
        print("Total:", total)

    elif choice == 4:
        break

    else:
        print("Invalid choice")
