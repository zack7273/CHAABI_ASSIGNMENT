"""
Q7. Calculate the factorial of a number using lambda function.
"""


factorial = lambda n: 1 if n == 0 else n * factorial(n-1)

# Example
number = 5
result = factorial(number)

print(result)




"""
The factorial function is defined using a lambda expression. A lambda expression is a short, one-line function that can be used to define a simple function.
The factorial function takes one argument: a number.
The factorial function returns the factorial of the number. The factorial of a number is the product of all the positive integers from 1 to the number.
The factorial function uses recursion to calculate the factorial of a number. Recursion is a method of solving a problem by breaking it down into smaller problems of the same type.
The factorial function has two cases:
If the number is 0, the factorial function returns 1.
If the number is greater than 0, the factorial function returns the number multiplied by the factorial of the number minus 1.
"""