# https://www.geeksforgeeks.org/find-k-numbers-occurrences-given-array/


from queue import PriorityQueue


a = [3, 1, 4, 4, 5, 2, 6, 1]


class Wrapper:
    def __init__(self, value):
        self.value = value
    
    def __lt__(self, next):
        return self.value[0] > next.value[0]


freq = {}

for i in a:
    if i in freq:
        freq[i] += 1
    else:
        freq[i] = 1

pq = PriorityQueue()

for k, v in freq.items():
    pq.put(Wrapper((v, k)))

for i in range(3):
    t = pq.get().value
    print(t)
