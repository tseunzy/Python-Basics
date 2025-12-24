

# Personal Finance Tracker
transactions = []

def add_transaction():
    amount = float(input("enter amount: "))
    type  = input("Enter category (savings, eating, clubbing etc): ")
    transactions.append({"amount": amount, "type": type})
    print(f"{amount} added to {type}.")

def view_balance(): # for all accumulated balance
    total = 0
    for t in transactions:
        total = total + t['amount'] # total balance
    print(f"Total balance: ${total}")

def analyze_transaction():
    categories = {}
    for t in transactions:
        type = t['type']
        amount = t['amount']
        if type in categories:
            categories[type] = categories[type] + amount # add amount if found
        else:
            categories[type] = amount # create 'type' and amount if not found
    print("Spending by category:")
    for type, amount in categories.items():
        print(f"  {type}: ${amount}")

while True:
    print("\nPersonal Finance Tracker")
    print("1. Add Money")
    print("2. View Balance")
    print("3. Analyze Spending")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == '1':
        add_transaction()
    elif choice == '2':
        view_balance()
    elif choice == '3':
        analyze_transaction()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
