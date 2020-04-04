import bisect
sorted_fruits = ['apple', 'banana', 'orange', 'plum']
index = bisect.bisect_left(sorted_fruits, 'banana')
# print(index)

sorted_fruits2 = ['apple', 'banana', 'banana', 'banana', 'banana', 'orange', 'plum']
index_left = bisect.bisect_left(sorted_fruits2, 'banana')
index_right = bisect.bisect_right(sorted_fruits2, 'banana')
index_main = bisect.bisect(sorted_fruits2, 'banana')
# print(index_left, index_right, index_main)
# print(sorted_fruits2[index_right], sorted_fruits2[index_main])


sorted_fruits3 = ['apple', 'banana', 'orange']
bisect.insort(sorted_fruits3, 'apricot')
bisect.insort_left(sorted_fruits3, 'watermelon')
bisect.insort_right(sorted_fruits3, 'plum')
print(sorted_fruits3)

"""
def find_index(elements, value):
    index = bisect.bisect_left(elements, value)
    if index < len(elements) and elements[index] == value:
        return index
"""

