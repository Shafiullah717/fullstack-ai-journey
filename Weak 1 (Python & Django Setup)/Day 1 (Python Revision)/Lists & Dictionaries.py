# print("Lists and Dictionaries in Python")
# Lists Ordered Collections
# Create a list

fruits = ["apple", "banana", "cherry", "date"]

# Access elements by index (starts at 0)
# print(fruits[0])    
# print(fruits[-1])    

# Modify an item
fruits[1] = "blueberry"
# print(fruits)       

# Add items
fruits.append("fig")       # Add to the end
fruits.insert(2, "mango")  # Insert at index 2

# Remove items
fruits.remove("cherry")    # Remove by value
popped_item = fruits.pop() # Remove last item ("fig")

# print(fruits)  

# fruits.append("Banana")
# print(fruits)
# fruits[0] = "Orange"
# fruits.insert(1, "Apple")
# print(fruits)
# fruits.remove("blueberry")
# print(fruits)
# popped = fruits.pop()
# print(popped)
# print(fruits)

# Now we extract the part of list using slicing [start : end : step]

numbers = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(numbers)

# print(numbers[2:5])
# print(numbers[::3])
# print(numbers[::-1])

# List Comprehension

squares = [x**2 for x in range(10)]
# print(squares)

even = [x for x in range(20) if x % 2 == 0]
# print(even)

# Dictionaries : key - value Pairs
# A Dictionry is an unordered, mutable collection of key : value pairs.

# Baic Dictionry Operations

# Create a dictionary
student = {
    "name": "Shafiullah ",
    "age": 21,
    "courses": ["Math", "Physics"]
}

# Access values using keys
print(student["name"])   
print(student.get("grade", "N/A"))  

# Add/update items
student["grade"] = "A"         # Add new key
student["age"] = 22            # Update existing key

# Remove items
del student["courses"]         # Delete key
popped_value = student.pop("age")  # Remove and return value

print(student)  

# Dictionary Comprehensions
# Squares of numbers 0-4
squares = {x: x**2 for x in range(5)}


# Convert list to dictionary (keys as indexes)
fruits = ["apple", "banana", "cherry"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}

