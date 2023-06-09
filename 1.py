"""

Q1:
Get your basics right - Implement selection sort algorithm in python. The function accepts a
list in the input and returns a sorted list.
E.g.
Input f1([5,416,54,21,6135,15,741]) should
Return [5, 15, 21, 54, 416, 741, 6135]


"""

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr



input_list = [5, 416, 54, 21, 6135, 15, 741]
sorted_list = selection_sort(input_list)
print(sorted_list)


"""
The code defines a function called selection_sort that takes a list of numbers as input.

The function starts a loop that goes through each number in the list.

Inside the loop, the code keeps track of the index of the smallest number found so far in the unsorted portion of the list.

Another loop starts, looking at the numbers after the current number in the outer loop, to find the smallest number.

If a smaller number is found, its index is updated as the new smallest index.

After the inner loop finishes, the smallest number in the unsorted portion is known, and it's swapped with the current number being examined in the outer loop.

The outer loop continues, and the process is repeated with the next number until all numbers have been examined.

Finally, the sorted list is returned.

In the main code, an example list is created: [5, 416, 54, 21, 6135, 15, 741].

The selection_sort function is called with this list, and the returned sorted list is stored in a variable.

The sorted list is then printed.

In simple terms, the code is sorting a list of numbers from smallest to largest using the selection sort algorithm. It repeatedly finds the smallest number in the unsorted portion and moves it to its correct position.

"""
