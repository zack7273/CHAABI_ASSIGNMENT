"""
Q3. Column Sorting, yay!
Given a list of dicts, write a program to sort the list according to a key given in input.
E.g.
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "fruit")
Should Output
[
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"}
]
AND
Input f([
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"},
{"fruit": "blueberry", "color": "blue"}
], "color")
Should Output
[
{"fruit": "blueberry", "color": "blue"},
{"fruit": "orange", "color": "orange"},
{"fruit": "apple", "color": "red"},
{"fruit": "banana", "color": "yellow"}
]
"""





def sort_list_of_dicts(data, key):
    sorted_data = sorted(data, key=lambda x: x[key])
    return sorted_data



data = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

# print(sorted(data.key))

sorted_data = sort_list_of_dicts(data, "fruit")
print(sorted_data)
# Output: [{'fruit': 'apple', 'color': 'red'}, {'fruit': 'banana', 'color': 'yellow'},
# {'fruit': 'blueberry', 'color': 'blue'}, {'fruit': 'orange', 'color': 'orange'}]

sorted_data = sort_list_of_dicts(data, "color")
print(sorted_data)
# Output: [{'fruit': 'blueberry', 'color': 'blue'}, {'fruit': 'orange', 'color': 'orange'},
# {'fruit': 'apple', 'color': 'red'}, {'fruit': 'banana', 'color': 'yellow'}]



"""
def sort_list_of_dicts(data, key):

This function takes two arguments: data is a list of dictionaries, and key is the name of the key that we want to sort the dictionaries by.


sorted_data = sorted(data, key=lambda x: x[key])

This line uses the sorted() function to sort the data list. The sorted() function takes two arguments: the iterable that we want to sort, and a key function. The key function is used to extract a value from each item in the iterable, and that value is used to sort the items. In this case, the key function is a lambda function that extracts the value of the key key from each dictionary in the data list.


return sorted_data

This line returns the sorted data list.


data = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]

This line creates a list of dictionaries. Each dictionary has two keys: fruit and color.


sorted_data = sort_list_of_dicts(data, "fruit")
print(sorted_data)

This line calls the sort_list_of_dicts() function to sort the data list by the fruit key. The output of the print() statement is a list of dictionaries, sorted by the fruit key.


sorted_data = sort_list_of_dicts(data, "color")
print(sorted_data)

This line calls the sort_list_of_dicts() function to sort the data list by the color key. The output of the print() statement is a list of dictionaries, sorted by the color key.



"""