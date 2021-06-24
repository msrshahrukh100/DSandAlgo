#  ps - find the longest subarray with sum == k

import sys
current_sum = 0

arr = [1, 2, 3, 4, 123, 1, 1, 1]

k = 10

i, j = 0, 0

answer = -sys.maxsize

while j < len(arr):
    current_sum += arr[j]

    if current_sum < k:
        j += 1

    elif current_sum == k:
        answer = max(answer, j-i)
        j += 1

    elif current_sum > k:

        while current_sum > k:
            current_sum -= arr[i]
            i += 1
        j += 1
