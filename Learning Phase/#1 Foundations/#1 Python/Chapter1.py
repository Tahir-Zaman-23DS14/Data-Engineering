

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

# Invalid names (will cause errors)
# 2name = "test"     # Cannot start with number
# first-name = "test" # Hyphen not allowed
# class = "Math"     # Cannot use reserved keywords
Example 5: Variable Operations
python
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
"""