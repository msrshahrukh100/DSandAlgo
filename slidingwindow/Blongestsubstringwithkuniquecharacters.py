# ps - find the longest substring with k unique characters

import sys

given_str = "asdfsdfdw"
k = input("enter the number of unique chars you're looking for")
freq = {}
answer = -sys.maxsize
i, j = 0, 0

while j < len(given_str):

    if given_str[j] in freq:
        freq[given_str[j]] += 1
    else:
        freq[given_str[j]] = 1

    if len(freq) < k:
        j += 1

    elif len(freq) == k:
        answer = max(answer, j - i)
        j += 1

    elif len(freq) > k:

        while len(freq) > k:
            freq[given_str[i]] -= 1
            if freq[given_str[i]] == 0:
                del freq[given_str[i]]
            i += 1
        j += 1
