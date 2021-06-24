# ps - given a string find the longest substring with all unique characters
import sys
given_str = "sadfasdfga"

answer = -sys.maxsize

i, j = 0, 0

freq = {}   # used for storing the frequencies

while j < len(given_str):

    if given_str[j] in freq:
        freq[given_str[j]] += 1
    else:
        freq[given_str[j]] = 1

    # if len(freq) > j - i + 1:   #  Not required
    #     j += 1

    if len(freq) == j - i + 1:
        answer = max(answer, j - i)

    elif len(freq) < j - i + 1:

        while len(freq) < j - i + 1:
            freq[given_str[i]] -= 1
            if freq[given_str[i]] == 0:
                del freq[given_str[i]]

            i += 1

    j += 1
