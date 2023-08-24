from collections import deque


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

def swap(stack):
    if len(stack) >= 2:
        stack[-2], stack[-1] = stack[-1], stack[-2]

stack = deque([1, 2, 3])
swap(stack)
print(stack)  # Output: deque([1, 3, 2])
