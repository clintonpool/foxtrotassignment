expenses = []
expense = input("Enter the expense name: ")
price = float(input("Enter the expense amount: "))
expense_item = {"expense": expense, "price": price}
budget_limit = 500  
if price > budget_limit:
    expense_item["is over the budget"] = True
    expenses.append(expense_item)
else:
    expense_item["is over the budget"] = False
    expenses.append(expense_item)

print(expenses)