# ====================== PYTHON DATA STRUCTURES ASSIGNMENT ======================

# ----------- DICTIONARY -----------

# 1. Create a dictionary called car with keys: "brand", "model", "year".
#    Give them values and print the dictionary.
# Answer no 1 here.
cars = { "Brand":  "Toyota", 
        "Model": "Corolla", 
        "Year": "2020" }
print(cars)


# 2. From a dictionary called book = {"title": "Python 101", "author": "James", "year": 2022},
#    print only the title and author.
# Answer no 2 here.
book = {"title": "Python 101", "author": "James", "year": 2022}
print(book["title"], book["author"])

# 3. Change the value of "year" in book to 2024 and print the dictionary.
# Answer no 3 here.
book["year"]=2024
print(book)
# 4. Add a new key "pages" with any number value to the dictionary book.
# Answer no 4 here.
#assign new key with a value in dictionary
book["pages"] =58
print(book)

# 5. Delete the "author" key from the dictionary book and print it.
# Answer no 5 here.
print(book.pop("author"))

# ----------- LIST -----------

# 6. Create a list of 5 countries and print the first and last country.
# Answer no 6 here.
Countries = ["Nigeria", "Ghana", "Kenya", "Togo", "Ethiopia",]
print(Countries[0], Countries[4])


# 7. Replace the 2nd item in your list of countries with "Canada".
# Answer no 7 here.
Countries[1] = "Canada"
print(Countries)
# 8. Delete the 3rd item in your list of countries.
# Answer no 8 here.
del Countries[2]
print(Countries)


# 9. Concatenate [10, 20, 30] with [40, 50, 60] and print the new list.
# Answer no 9 here.
new_list = [10, 20, 30] + [40, 50, 60]
print(new_list)

# 10. Check if "Kenya" exists inside your list of countries and print the result.
# Answer no 10 here.
print("Kenya" in Countries)

# 11. Create a list with the word "Hello" repeated 4 times.
# Answer no 11 here.
greetings = ["Hello"] * 4
print(greetings)

# 12. Use append() to add "Japan" to your list of countries.
# Answer no 12 here.
Countries.append("Japan")

# 13. Use insert() to add "Brazil" at position 2 in your list of countries.
# Answer no 13 here.
Countries.insert(1, "Brazil")

# 14. Use pop() to remove the last item from a list of numbers = [100, 200, 300, 400].
# Answer no 14 here.
numbers = [100, 200, 300, 400]
numbers.pop(3)

# 15. Use remove() to delete the number 200 from the list numbers = [100, 200, 300, 400].
# Answer no 15 here.
numbers.remove(200)
print(numbers)

# ----------- NESTED LIST -----------

# 16. Given nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]
#     - Print the value "b"
#     - Add "d" into the "letters" list
# Answer no 16 here.
nested = [1, [2, 3, {"letters": ["a", "b", "c"]}], 4]

print(nested[1][2]["letters"][1])



# ----------- TUPLE -----------

# 17. Create a tuple of 4 animals and print the second animal.
# Answer no 17 here.
animals = ("dogs", "goat", "chicken", "Turkey",)
print(animals[1])

# 18. Try to change one value in the tuple. What happens? (Write the answer in a comment)
# Answer no 18 here.
#animals[2] = "Lion"
#print(animals)
#TypeError: 'tuple' object does not support item assignment

# 19. Count how many times "cat" appears in the tuple: pets = ("cat", "dog", "cat", "bird").
# Answer no 19 here.
pets = ("cat", "dog", "cat", "bird")
print(pets.count("cat") )

# ----------- SET -----------

# 20. Create two sets:
#     set1 = {"apple", "banana", "cherry"}
#     set2 = {"banana", "mango", "cherry"}
#     - Find the intersection
#     - Find the union
#     - Find the difference (set1 - set2)
# Answer no 20 here.
set1 = {"apple", "banana", "cherry"}
set2 = {"banana", "mango", "cherry"}
print(set1.intersection (set2))
print(set1.union (set2))
print(set1.difference(set2))
