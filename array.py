import array
from copy import *


arr = array.array("i", [1,3, 5,6 ,7, 8])

print(arr)

l = [1,3,4,5,6]

l.insert(3, 8)

print(l)

j = copy(l)
j.insert(1, 7)

print(l, j)

# array and list are same

# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the first item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list