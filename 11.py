"""
Q11. Something fishy there -
Find output of following:
def f(x,l=[]):
for i in range(x):
l.append(i*i)
print(l)
f(2)
f(3,[3,2,1])
f(3)
"""


"""
def f(x,l=[]):

This function takes two arguments: x is the number of elements to generate, and l is a list. The default value of l is an empty list.


for i in range(x):
l.append(i*i)

This loop iterates over the range x and appends the square of each number to the list l.


print(l)

This prints the list l.


f(2)

This calls the f() function with the argument 2. The output of this call is [0, 1].


f(3,[3,2,1])

This calls the f() function with the arguments 3 and [3, 2, 1]. The output of this call is [3, 2, 1, 0, 1, 4].


f(3)

This calls the f() function with the argument 3. The output of this call is [0, 1, 0, 1, 4]
"""
