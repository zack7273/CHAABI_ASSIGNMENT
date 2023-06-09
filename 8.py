"""
Q8. Some neat tricks up her sleeve:
Looking at the below code, write down the final values of A0, A1, ...An
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])
A8 = map(lambda x: x*2, [1,2,3,4])
A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])"""





"""

A0 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
A1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
A2 = [1, 2, 3, 4, 5]
A3 = [1, 2, 3, 4, 5]
A4 = [1, 2, 3, 4, 5]
A5 = {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
A6 = [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
A7 = 48
A8 = [2, 4, 6, 8]
A9 = [“want”, “to”, “learn”, “python”]
A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
This line of code creates a dictionary called A0. The dictionary maps the strings 'a', 'b', 'c', 'd', and 'e' to the numbers 1, 2, 3, 4, and 5, respectively.


A1 = range(10)

This line of code creates a list called A1. The list contains the numbers from 0 to 9.


A2 = sorted([i for i in A1 if i in A0])

This line of code sorts the list A1 and then filters it to only include the numbers that are also in the dictionary A0.


A3 = sorted([A0[s] for s in A0])

This line of code sorts the list of numbers that are the values of the dictionary A0.


A4 = [i for i in A1 if i in A3]
This line of code filters the list A1 to only include the numbers that are also in the list A3.


A5 = {i:i*i for i in A1}

This line of code creates a dictionary called A5. The dictionary maps the numbers in the list A1 to their squares.


A6 = [[i,i*i] for i in A1]

This line of code creates a list of lists called A6. Each list in A6 contains two numbers: the first number is the number in the list A1, and the second number is the square of the number in the list A1.


A7 = reduce(lambda x,y: x+y, [10,23, -45, 33])

This line of code uses the reduce() function to add the numbers in the list [10,23,-45,33] together. The reduce() function repeatedly applies the function lambda x,y: x+y to the elements of the list. The function lambda x,y: x+y adds the two numbers together.


A8 = map(lambda x: x*2, [1,2,3,4])

This line of code uses the map() function to multiply each number in the list [1,2,3,4] by 2. The map() function applies the function lambda x: x*2 to each element of the list. The function lambda x: x*2 multiplies the number by 2.


A9 = filter(lambda x: len(x) >3, [“I” , “want”, “to”, “learn”, “python”])

This line of code uses the filter() function to filter the list [“I” , “want”, “to”, “learn”, “python”] to only include the strings whose lengths are greater than 3. The filter() function filters the list to only include the elements that satisfy the condition len(x) >3. The condition len(x) >3 checks if the length of the string is greater than 3.

"""