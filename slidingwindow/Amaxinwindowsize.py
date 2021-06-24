# ps - given a list of arr find the maximum in a given window size for all windows

queue = [-sys.maxsize]

arr = []
i, j = 0, 0
k = input("enter length of window")

answer = []

while j < len(arr):

    if arr[j] > queue[-1]:
        while queue and arr[j] > queue[-1]:
            queue.pop()

    queue.append(arr[j])

    if j - i == k:
        answer.append(queue[0])
        if queue[0] == arr[i]:
            queue.pop(0)

        i += 1

    j += 1
