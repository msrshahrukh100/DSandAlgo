# ps - pick toys in continuity and maximum of 2 different types of toys

import sys

store = "abacsasd"

i, j = 0, 0

freq = {}

k = 2

answer = -sys.maxsize

while j < len(store):

    if store[j] in freq:
        freq[store[j]] += 1
    else:
        freq[store[j]] = 1

    if len(freq) < k:
        j += 1

    elif len(freq) == k:
        answer = max(answer, j - i + 1)
        j += 1

    elif len(freq) > k:
        while len(freq) > k:
            freq[store[i]] -= 1
            if freq[store[i]] == 0:
                del freq[store[i]]

            i += 1
        j += 1
