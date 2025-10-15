#1. Create a list called expenses. It's going to be a list of dictionary in this format e.g [{"expense": "Transportation", "price": 400}].
#2. create inputs: expense, price.
#3. Create a dictionary with the keys and values of expense and price.
#4. Write an if else statement. If price is greater than (put your price), update the dictionary with the key "is_over_the_budget", set True and append to expenses.
  # Else add the same type of key "is_over_the_budget", set to False and append to expenses.
#5. Debug at the end to check if your code is working as expected. let us start over answering exactly what is expected 

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