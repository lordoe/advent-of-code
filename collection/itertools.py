from itertools import zip_longest, accumulate

# normal zip funciton stops when the shorter list ends
# zip_longest can be used to solve this
print(">>> list(zip_longest([1,2,3,4,5],[1,2,3]))")
print(">>>", list(zip_longest([1,2,3,4,5],[1,2,3])))
# >>> [(1, 1), (2, 2), (3, 3), (4, None), (5, None)]

# accumulate (like sum but with previous results and custom lambda definable)
print("\n>>> list(accumulate([1,1,1,1])")
print(">>>", list(accumulate([1,1,1,1])))
# >>> [1, 2, 3, 4]

b = [1,2,3,4,5]
assert(sum(b) == list(accumulate(b))[-1])
print(list(accumulate([10,10,10,10], lambda x,y: (x+y)%3)))
