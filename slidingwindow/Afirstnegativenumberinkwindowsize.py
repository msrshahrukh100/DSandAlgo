# ps - of all substrings of length k find the first negative number


queue = []

arr = []
k = input("Window size")
i, j = 0, 0

answer = []

while j < len(arr):
    if arr[j] < 0:
        queue.append(arr[j])

    if j - i + 1 == k:
        if queue:
            answer.append(queue[0])
        else:
            answer.append(0)

        if arr[i] == queue[0]:
            queue.pop(0)
        i += 1

    j += 1
