"""
Q4.
The power of one line -
Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
key becomes value. The function's body shouldn't have more than one statement.
f({
"key1": "value1",
"key2": "value2",
"key3": "value3",
"key4": "value4",
"key5": "value5"
})
 should return
{
"value1": "key1",
"value2": "key2",
"value3": "key3",
"value4": "key4",
"value5": "key5"
}

"""


def f(d):
  return {v: k for k, v in d.items()}


"""This function uses a dictionary comprehension to create a new dictionary where the keys and values are swapped. The items() method on the dictionary d returns a list of tuples, where each tuple contains a key and a value. The dictionary comprehension then iterates over this list of tuples and creates a new dictionary where the key from each tuple is used as the new key and the value from each tuple is used as the new value."""

d = {
  "key1": "value1",
  "key2": "value2",
  "key3": "value3",
  "key4": "value4",
  "key5": "value5"
}

new_dict = f(d)

print(new_dict)




"""

The f() function takes a dictionary as input.
The items() method on the dictionary returns a list of tuples, where each tuple contains a key and a value.
The dictionary comprehension creates a new dictionary, where the keys are the values from the original dictionary, and the values are the keys from the original dictionary.
The return statement returns the new dictionary.



The for loop iterates over the list of tuples returned by the items() method.
The v variable represents the value from each tuple.
The k variable represents the key from each tuple.
The {v: k} expression creates a new dictionary entry, where the key is v and the value is k.
The for loop is executed once for each tuple in the list, so the dictionary comprehension creates a new dictionary with one entry for each key-value pair in the original dictionary.


"""
