""""
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

expenses = []

def add_expenses(expenses, name, amount, category):
    myexpenses = {"name": name, "amount": amount, "category": category }
    expenses.append(myexpenses)
    return expenses