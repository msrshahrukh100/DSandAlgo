# ps - find the maximum sum possible with a given window size
import sys

answer = -sys.maxsize

arr = []

i = 0
j = k

s = sum(arr[i:j])

while j < len(arr):
    answer = min(answer, s)
    s -= arr[i]
    s += arr[j]
    j += 1
    i += 1


----


i = 0
j = 0
s = 0
while j < len(arr):
    s = s + arr[j]

    if (j - i + 1) < k:
        j += 1
    elif j - i + 1 == k:
        answer = max(answer, s)
        s -= arr[i]
        i += 1
        j += 1
