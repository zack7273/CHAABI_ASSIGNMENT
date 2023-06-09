"""
Q6. Every other sub-list
Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
contain every second element.
E.g.
Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
Return [5, 11, 17, 23]

"""

def get_sublist(lst, start_index, end_index):
    sub_list = lst[start_index:end_index+1:2]
    return sub_list

# Example usage
lst = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]
start_index = 2
end_index = 9

result = get_sublist(lst, start_index, end_index)
print(result)


"""

The get_sublist() function takes three arguments: a list, a start index, and an end index.
The lst variable refers to the list that was passed to the function.
The start_index variable refers to the index of the first element to include in the sub-list.
The end_index variable refers to the index of the last element to include in the sub-list.
The sub_list variable is a new list that will contain the results.
The lst[start_index:end_index+1:2] expression creates a new list that contains every other element from the original list, starting at the start index and ending at the end index, with a step size of 2.
The return sub_list statement returns the sub_list variable.
The lst variable is initialized with the list [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41].
The start_index variable is initialized with the value 2.
The end_index variable is initialized with the value 9.
The result variable is assigned the value of the get_sublist() function, which returns the sub-list [5, 11, 17, 23].
The print(result) statement prints the result variable, which is the sub-list [5, 11, 17, 23]

"""