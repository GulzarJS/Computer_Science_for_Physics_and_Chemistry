# Exercise 1 - Factorial
# Write a function that takes an integer as input and that returns its factorial ( n! ).
# Try two ways to implement these functions:
#
# One with dynamic evaluations using eval () function.
# One with a recursive function call.

# Factorial function => with eval()

def fuctorial_str(number):
    string = " "
    for i in range(1, number + 1):
        if i != number:
            string = string + str(i) + " * "
        else:
            string = string + str(i)
    return string

def factorial_eval(number):
    fuctorial = eval(fuctorial_str(number))
    return fuctorial

# Factorial function => with recursive function call
def factorial_rec(number):
     return 1 if (number == 1 or number == 0) else number * factorial_rec(number - 1)

# Function calls
number = 5
print(number, "! =", fuctorial_str(number), "=", factorial_eval(number))
print(number, "! =", fuctorial_str(number), "=", factorial_rec(number))