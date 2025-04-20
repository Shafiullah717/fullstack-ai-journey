# Functions in Python 
# print("Functions in Python")
def greet(name = "Ahsan"):
    return f"How are you? ,{name}!"

# print(greet("Ahsan"))

def Result(name):
    return f"Your Current CGPA is 3.5 {name}"
# print(Result("Shafiullah"))

def fruits(Name):
    return f"and the fruit name is {Name}"
# print(fruits("Orange"))    

# Arguments in Functions 
# 1> ( * ) fort any number of positional arguments 
def total_numbers(*arguments):
    count = 0
    for num in arguments:
        count += num
    return count
# print(total_numbers(1,2,3,4))    
# print(total_numbers(33,44,55,66))

# 2> (**) variable keyword arguments 
def Data(**Profile):
    for key, value in Profile.items():
        print(f"{key} : {value}")

# Data(name = "Shafiullah", Age = 22, City = "Pakistan")

# 3> Now we use box (*) , (**) in same Program
def processdata(name, *args, status = "Active", **kwargs):
    print(f"Name : {name}") 
    print(f"Positional Numbers : {args}")
    print(f"Status : {status}")
    # print(f"Keywords : {kwargs}")
    for key, value in kwargs.items():
        print(f"{key} : {value}")

# processdata("Shafiullah", 10, 20, role = "Admin", City = "Khairpur")    

# Lamda Functions in Python
# basic
def add(a, b):
    return(a + b)
# print(add(10,20))    
# Using Lamda
add = lambda a,b : a+b
# print(add(10, 20))

# Sort a list of tuples by the second element
points = [(1, 4), (3, 1), (2, 5)]
sorted_points = sorted(points, key=lambda point: point[1])
# print(sorted_points)

# Double each number in a list
numbers = [1, 2, 3]
doubled = list(map(lambda x: x * 2, numbers))
# print(doubled)

# Filter even numbers
even = list(filter(lambda x: x % 2 == 0, numbers))
# print(even)

# Lamda also use in conditional logic
is_even = lambda x : "even" if x % 2 == 0 else "odd"
print(is_even(5))