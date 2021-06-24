# https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/

import heapq
numbers = []
for n in [1, 2, 3, 4, 5, 6]:
    # n = int(input("Enter the next number: "))
    if len(numbers) < 4:
        heapq.heappush(numbers, n)
    else:
        # item = numbers[0]
        # if n > item:
        #     heapq.heappop(numbers)
        #     heapq.heappush(numbers, n)
        heapq.heappush(numbers, n)
        heapq.heappop(numbers)

    if len(numbers) == 4:
        tle = numbers[0]
        print("3rd largest element is ", tle)
    else:
        print("-1")


