# https://www.geeksforgeeks.org/kth-largest-element-in-a-stream/

import heapq
numbers = []
while True:
    n = int(input("Enter the next number: "))
    if len(numbers) < 3:
        heapq.heappush(numbers, n)
    else:
        item = numbers[0]
        if n > item:
            heapq.heappop(numbers)
            heapq.heappush(numbers, n)

    if len(numbers) > 2:
        tle = numbers[0]
        print("3rd largest element is ", tle)
