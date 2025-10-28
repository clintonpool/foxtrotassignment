#1. Create a list called expenses. It's going to be a list of dictionary in this format e.g [{"expense": "Transportation", "price": 400}].
#2. create inputs: expense, price.
#3. Create a dictionary with the keys and values of expense and price.
#4. Write an if else statement. If price is greater than (put your price), update the dictionary with the key "is_over_the_budget", set True and append to expenses.
  # Else add the same type of key "is_over_the_budget", set to False and append to expenses.
#5. Debug at the end to check if your code is working as expected. let us start over answering exactly what is expected 

# expenses = []
# while True:
#     expense = input("Enter the expense name: ")
#     price = float(input("Enter the expense amount: "))
#     expense_item = {"expense": expense, "price": price}
#     budget_limit = 500  
#     if price > budget_limit:
#         expense_item["is over the budget"] = True
#         expenses.append(expense_item)
#     else:
#         expense_item["is over the budget"] = False
#         expenses.append(expense_item)

#     print(f"{expenses} has been added.")
#     option = input(f"Do you want to continue?(choosey/n): ")
#     if option =="y":
#         continue
#     elif option == 'n':
#         for item in expenses:
#             print(f"Expense:{item["expense"]}, Price: {price}")
#         break
#     else:
#             print("Invalid option")



# books = []  # Empty list to store all the books

# while True:
#     # Ask for book details
#     title = input("Enter the book title: ")
#     pages = int(input("Enter the number of pages: "))

#     # Create a dictionary for the book
#     book_item = {"title": title, "pages": pages}

#     # Check if the book is long or not
#     if pages > 300:
#         book_item["long"] = True
#     else:
#         book_item["long"] = False

#     # Add the book to the list
#     books.append(book_item)

#     print(f"'{title}' has been added to your list.\n")

#     # Ask if the user wants to continue
#     option = input("Do you want to add another book? (y/n): ").lower()

#     if option == "y":
#         continue
#     elif option == "n":
#         print("\nYour Book List:")
#         for book in books:
#             print(f"Book: {book['title']}, Pages: {book['pages']}, Long: {book['long']}")
#         break
#     else:
#         print("Invalid option. Please enter 'y' or 'n'.")


# Movies=[]
# while True:
#     title = input("What is the title of your movie: ")
#     rating = int(input("what rating eould you give the movie: "))

#     good_movie = {"title" : title, "rating" : rating}
#     if rating > 7 :
#        good_movie['good'] = True
#     else:
#         good_movie["good"] = False

#     Movies.append(good_movie)
#     print(f"'{title}' has been added.\n")

#     print(f"'{title}' has been added.\n")

#     option = input("Do you want to add another movie? (y/n): ").lower()

#     if option == "y":
#         continue
#     elif option == "n":
#             print("\nYour Movie List:")
#             for movie in Movies:
#                 print(f"Movie: {movie['title']}, Rating: {movie['rating']}, Good Movie: {movie['good']}")
#     break

# else:
#      print("Invalid option. Please enter 'y' or 'n'.")



grocery = []
while True:
    item_name = input("what is the name of the item? : " )
    price = float(input("type in the price of the item: "))

    item = {"item_name" : item_name, "price" : price }

    if price > 1000:
          item["price"] == True
    else:
        item["price"] == False
        grocery.append(item)    
        option = input('do you want to add more to the list: y/n').lower()
        
    if option == "y":
             continue
    elif option == "n":
            print('Your grocery list :')
            for items in grocery:
                 print (f"Grocies: {grocery['item_name']}, Price: {grocery['price']}, Item: {grocery["item"]}")
                 
                 break
            else:
             print("Invalid option. Please enter 'y' or 'n'.")
            
                            



















