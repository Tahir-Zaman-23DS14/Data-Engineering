

# in Chapter1 we will cover the basics of Python programming language. For Data Engineering


# WE Cover these Topics: theoretical with Practises
# 1. print Function,
# 2. Data Types,
# 3. Variables,
# 4. Input Function,





                                            #######################################################################################
# 1. print Function 
""" A built-in function that displays messages on the output screen to communicate with users.  """

"""
Let’s explain it in a different, simpler way using a real-life analogy.

Think of a function like a kitchen machine:
   1 You give it some ingredients (inputs).
   2 It does something (processes the ingredients)
   3 Sometimes it gives you something back (output).

For example, print() is like a speaker in your kitchen: you give it a message, and it announces it aloud. It doesn’t return anything—you just hear it.
    print("Hello, Tahir!")  # The speaker says the message

    Output:
    Hello, Tahir!


Now, if you create your own function:

    def add_numbers(a, b):  # kitchen machine for adding
    return a + b        # gives the sum as output

    result = add_numbers(5, 3)  # use the machine
    print(result)               # show the output

    Output:
    8

    Here, add_numbers is your own machine.
    a and b are ingredients (inputs).
    return a + b is the result it gives back.
    Then we use print() to show it to the user.

So the key idea is:
Functions = machines that do tasks.

print() = a function that shows messages to the user. """

# Syntax of print function:

# print Function

    #Please Remove multiline comment """code""" to run the code below

"""     
print("Hello, World!") 
print("Hello", "World")


print("Python")
print("Learning")


print("Python", end=" ")
print("Programming")

print(10 + 20)
print("10 + 20")

print("A", "B", "C", sep="-")

x = 5
print(x)



x = 5
y = 10
print(x, y)


print("Line1\nLine2")
"""
                                            #######################################################################################
# 2. Data Types
""" 
## What is a Data Type?
A data type defines what kind of data a variable can store and what operations can be performed on it.
It tells Python how to handle the data in memory.

Think of it like different containers:
 1.A number container for calculations
 2.A text container for words
 3.A true/false container for decisions

## Main Data Types

1. Integer (int)

    Definition:
    Whole numbers without decimals (positive, negative, or zero)
    Use: For counting, calculations with whole numbers

        age = 25          # Positive integer
        temperature = -5  # Negative integer  
        count = 0         # Zero
 
 
 2. Float (float)

    Definition:
    Numbers with decimal points
    Use: For measurements, precise calculations

        price = 19.99     # Decimal number
        pi = 3.14159      # Mathematical constant
        height = 1.75     # Measurement


3. String (str)

    Definition:
    Text data (sequence of characters)
    Use: For names, messages, any text

        name = "Alice"      # Text in double quotes
        city = 'New York'   # Text in single quotes
        message = "Hello!"  # Any text content

4. Boolean (bool)
    
    Definition:
    Represents True or False values
    Use: For conditions, switches, yes/no decisions

       is_student = True    # Yes/true condition
        is_raining = False   # No/false condition
        is_empty = False     # Another false value

        
###Quick Comparison###

# Examples side by side
age = 25             # int - whole number
price = 29.99        # float - decimal number  
name = "John"        # str - text
is_active = True     # bool - true/false

# Check types
print(type(age))       # <class 'int'>
print(type(price))     # <class 'float'>
print(type(name))      # <class 'str'>
print(type(is_active)) # <class 'bool'>

Simple Rules
    int → Whole numbers: 10, -5, 0
    float → Decimal numbers: 3.14, -2.5, 0.0
    str → Text in quotes: "hello", 'Python'
    bool → Only True or False (case-sensitive)

That's it! These 4 are the most essential data types you'll use every day in Python.
""" 

                                            #######################################################################################

# 3. Variables
""" 
Variables in Python are like named containers that store data values.
Unlike some other languages, Python variables don't need explicit declaration of type - the type is dynamically inferred from the value you assign.

Key Characteristics:
 1 Dynamic Typing: Variables can change type during execution.
 2 No Declaration Needed: Just assign a value.
 3 Case Sensitive: age, Age, and AGE are different variables.
 4 Reference to Objects: Variables store references to objects in memory.

Basic Examples
Example 1: Simple Variable Assignment
# Creating variables
       name = "Alice"          # String
       age = 25                # Integer
       height = 5.6            # Float
       is_student = True       # Boolean
       print(name)            # Output: Alice
       print(age)             # Output: 25
       print(type(height))    # Output: <class 'float'>

Example 2: Dynamic Typing
# Variable can change type

       x = 10                 # x is integer
       print(type(x), x)      # Output: <class 'int'> 10
    
        x = "Hello"            # Now x is string
       print(type(x), x)      # Output: <class 'str'> Hello
    
       x = 3.14               # Now x is float
       print(type(x), x)      # Output: <class 'float'> 3.14
       

Example 3: Multiple Assignment
# Assign multiple variables in one line
  
        a, b, c = 10, 20, 30
        print(a, b, c)  # Output: 10 20 30

# Swap values easily
        x, y = 5, 10
        x, y = y, x      # Swap without temporary variable
        print(x, y)      # Output: 10 5

# Assign same value to multiple variables
        p = q = r = 100
        print(p, q, r)   # Output: 100 100 100


Example 4: Variable Naming Rules
# Valid variable names
        first_name = "John"
        _last_name = "Doe"
        age2 = 30       # Numbers allowed but not at start
        PI_VALUE = 3.14 # Constants often in uppercase

Example 5: Variable Operations

# Arithmetic operations
        num1 = 15
        num2 = 4

        sum_result = num1 + num2
        difference = num1 - num2
        product = num1 * num2
        quotient = num1 / num2      # Float division
        floor_div = num1 // num2    # Integer division
        remainder = num1 % num2     # Modulus

        print(f"Sum: {sum_result}")        # Output: Sum: 19
        print(f"Quotient: {quotient}")     # Output: Quotient: 3.75
        print(f"Remainder: {remainder}")   # Output: Remainder: 3

# String operations
        greeting = "Hello"
        name = "Alice"
        message = greeting + " " + name + "!"
        print(message)  # Output: Hello Alice!

-----------------------------------------------------------------------
        

# Invalid names (will cause errors)
# 2name = "test"     # Cannot start with number
# first-name = "test" # Hyphen not allowed
# class = "Math"     # Cannot use reserved keywords
"""
                                            #######################################################################################

# 4. Input Function
"""
Getting Input from Users
1. Use the input() function to get text input from the user.

    # Basic Syntax
      variable_name = input("Prompt message: ")

      Examples
        1. Simple Text Input

    # Get user's name
       name = input("Enter your name: ")
       print(f"Hello, {name}!")

       
2. Number Input (Convert from string)

    # Input returns string, convert to int for numbers
        age = input("Enter your age: ")
        age = int(age)  # Convert string to integer
        print(f"You are {age} years old.")

    # Shorter way:
        age = int(input("Enter your age: "))


3. Float Input

     # For decimal numbers
         price = float(input("Enter price: $"))
         print(f"The price is ${price:.2f}")

     
     
4. Multiple Inputs

    # Get multiple values
        name = input("What's your name? ")
        age = int(input("How old are you? "))
        city = input("Where do you live? ")
        print(f"{name} is {age} years old and lives in {city}.")

5. Input with Different Data Types

    # Get various types of data
        product = input("Product name: ")  # str
        quantity = int(input("Quantity: "))  # int
        price = float(input("Price per item: "))  # float
        in_stock = input("In stock? (yes/no): ").lower() == "yes"  # bool

        print(f"{quantity} x {product} = ${quantity * price}")
"""