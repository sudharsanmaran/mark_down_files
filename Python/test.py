from collections import defaultdict, deque
from itertools import count, cycle, repeat


# def roundrobin(*iterables):
#     "roundrobin('ABC', 'D', 'EF') --> A D E B F C"
#     iterators = deque(map(iter, iterables))
#     while iterators:
#         try:
#             while True:
#                 yield next(iterators[0])
#                 iterators.rotate(-1)
#         except StopIteration:
#             # Remove an exhausted iterator.
#             iterators.popleft()


# print(list(roundrobin('ABC', 'D', 'EF')))

# def delete_nth(d, n):
#     d.rotate(-n)    # Rotate the deque to bring the nth element to the left
#     d.popleft()      # Remove the leftmost element (the nth element)
#     d.rotate(n)      # Reverse the rotation to restore the original order

# d = deque([1,2,3,4,5])
# delete_nth(d, 2)
# print(d)

# def swap(stack):
#     if len(stack) >= 2:
#         stack[-2], stack[-1] = stack[-1], stack[-2]

# stack = deque([1, 2, 3])
# swap(stack)
# print(stack)  # Output: deque([1, 3, 2])


# d = {'a': 1, 'b': 2, 'c': 3}
# # k = next(iter(d))
# # val = d.pop(k)

# first_value = (k := next(iter(d)), v := d.pop(k), v * 2)

# print("First key:", k)
# print("First value:", first_value[1])
# print("Square of popped value:", first_value[2])
# print("Modified dictionary:", d)

# class Mydict(dict):
#    def __len__(self) -> int:
#       print("Mydict.__len__ called")
#       return super().__len__()
   

# a = Mydict((('a', 1), ('b', 2)))
# a['a'] = 1
# a['b'] = 2
# print(len(a))

from itertools import accumulate ,chain
import operator
# print(list(accumulate([1, 2, 3, 4, 5], func=operator.mul)))

from functools import reduce

numbers = [1, 2, 3, 4, 5]
n2 = [1, 2, 3, 4, 5]

n_n = [[1,2,3], [2,3,4], [3,4,5]]

print(list(chain(numbers, n2)))
print(list(chain.from_iterable(n_n)))