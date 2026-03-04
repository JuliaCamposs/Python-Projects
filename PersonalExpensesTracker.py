"""
Functions needed: 

# 1. add_expense(expenses, name, amount, category)
#    → creates a dictionary and adds it to the expenses list

# 2. view_expenses(expenses)
#    → prints all expenses in a readable format

# 3. total_spending(expenses)
#    → adds up all amounts and returns the total

# 4. spending_by_category(expenses, category)
#    → returns total spent in a specific category (e.g. "Food")

# 5. most_expensive(expenses)
#    → finds and returns the most expensive expense

# 6. main()
#    → ties everything together, asks user for input, shows a menu

"""

# step 1 

def add_expenses(expenses, name, amount, category):
    myexpenses = {"name": name, "amount": amount, "category": category }
    expenses.append(myexpenses)
    return expenses

# step 2

def view_expenses(expenses):
    for myexpenses in expenses:
        print(f"Name: {myexpenses['name']} | Amount: {myexpenses['amount']} | Category: {myexpenses['category']}")

# step 3

def total_spending(expenses):
    total = 0
    for myexpenses in expenses:
        total +=  myexpenses['amount']
    return total

# step 4

def spending_by_category(expenses, category):
    total = 0 
    for myexpenses in expenses:
        if myexpenses['category'] == category:
            total += myexpenses['amount']
    return total 

# step 5

def most_expensive(expenses):
        return max(expenses, key=lambda x: x['amount']) # Finding the item with the maximum value in a list

# step 6 

def main():
    expenses = []
    while True:
        print("1. Add expense")
        print('2. View expenses')
        print('3. Total spending')
        print('4. Spending by category')
        print('5. Most expensive')
        print('6. Quit')
    
        choice = input('Pick an option:').strip()

        if choice == '6':
            print('Goodbye, see you later!')
            break 

        elif choice == '1':
            name = input("Expense name: ")
            amount = float(input("Amount: "))
            category = input("Category: ")
            expenses = add_expenses(expenses, name, amount, category)

        elif choice == '2':
            view_expenses(expenses)

        elif choice == '3':
            print(f"Your total spending is: {total_spending(expenses)}")

        elif choice == '4':
            ask = input('Type category:')
            print(spending_by_category(expenses, ask))
        
        elif choice == '5':
            print(most_expensive(expenses))

main() # calling the function to show the options 



