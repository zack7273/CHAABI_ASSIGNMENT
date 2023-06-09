"""
Q.5: 

Common, Not Common
Given 2 lists in input. Write a program to return the elements, which are common to both
lists(set intersection) and those which are not common(set symmetric difference) between the
lists.
Input:
Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
Art Online","Bleach","Dragon Ball Z","One Piece"]
must_watch = ["Full Metal Alchemist","Code Geass","Death
Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
On Titan"]
f(mainstream, must_watch) should return:
["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
"One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]
"""


def compare_lists(list1, list2):
    common_elements = list(set(list1) & set(list2))
    uncommon_elements = list(set(list1) ^ set(list2))
    return common_elements, uncommon_elements

mainstream = ["One Punch Man", "Attack On Titan", "One Piece", "Sword Art Online", "Bleach", "Dragon Ball Z", "One Piece"]
must_watch = ["Full Metal Alchemist", "Code Geass", "Death Note", "Stein's Gate", "The Devil is a Part Timer!", "One Piece", "Attack On Titan"]

common, uncommon = compare_lists(mainstream, must_watch)

print("Common Elements:", common)
print("Uncommon Elements:", uncommon)


# The mainstream variable is a list of anime shows that are popular with mainstream audiences.
# The must_watch variable is a list of anime shows that are considered to be must-watch shows.

# The common variable is assigned the value of the compare_lists() function, which returns a list of the common elements in the two lists.
# The uncommon variable is assigned the value of the compare_lists() function, which returns a list of the uncommon elements in the two lists.



"""
The compare_lists() function takes two lists as arguments and returns two lists: one list of the common elements in the two lists, and one list of the uncommon elements in the two lists.
The common_elements variable is a list that will contain the common elements in the two lists.
The uncommon_elements variable is a list that will contain the uncommon elements in the two lists.
The set() function is used to convert the two lists to sets. A set is a collection of unique elements.
The & operator is used to find the intersection of the two sets. The intersection of two sets is the set of elements that are in both sets.
The ^ operator is used to find the difference of the two sets. The difference of two sets is the set of elements that are in one set but not in the other set.
The list() function is used to convert the two sets to lists.
The return statement returns the two lists of common and uncommon elements.

"""


