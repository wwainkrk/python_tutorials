import collections

lst = collections.deque()                   # collections.deque - source of double-linked queue

# Inserting elements at the front
# or back takes O(1) time:
lst.append('B')
lst.append('C')
lst.appendleft('A')

print(lst)

# However, inserting elements costs
# O(n) time, list follow for each element:
lst.insert(2, 'X')

print(lst)

# Removing elements at the front
# or back takes O(1) time:
lst.pop()
lst.popleft()

print(lst)

# Removing elements, similar like inserting
# takes O(n) by key, node after node
del lst[1]
lst.remove('B')

# Deques can be reversed in-place:
lst_two = collections.deque(['A', 'X', 'B', 'C'])
lst_two.reverse()

print(lst_two)

# Searching
print(lst_two.index('X'))




