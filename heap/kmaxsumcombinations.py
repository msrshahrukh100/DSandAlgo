# https://www.geeksforgeeks.org/k-maximum-sum-combinations-two-arrays/

from queue import PriorityQueue

class Wrapper:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, other):
        return self.value[0] > other.value[0]

a = [1, 4, 2, 3]
b = [2, 5, 1, 6]


a.sort(reverse=True)
b.sort(reverse=True)


pq = PriorityQueue()

pq.put(Wrapper((a[0] + b[0], (0, 0))))
print(a)
print(b)
taken = []
for i in range(4):
    item = pq.get()
    item = item.value
    indices = item[1]
    taken.append(indices)
    print(item[0], item[1])
    # print(taken, "-- taken")

    if (indices[0] + 1, indices[1]) not in taken:
        next_sum = a[indices[0] + 1] + b[indices[1]]
        next_indices = (indices[0] + 1, indices[1])
        pq.put(Wrapper((next_sum, next_indices)))
    
    if (indices[0], indices[1] + 1) not in taken:
        next_sum = a[indices[0]] + b[indices[1] + 1]
        next_indices = (indices[0], indices[1] + 1)
        pq.put(Wrapper((next_sum, next_indices)))


