# ps = given a string count all occurrences of an anagrams of a given word

from collections import defaultdict
pattern = ""
s = ""
k = len(pattern)
i, j = 0, 0
answer = []


def are_anagrams(a, b):
    return "".join(sorted(a)) == "".join(sorted(b))


while j < len(s):

    if j - i == k:
        if are_anagrams(s[i:j], pattern):
            answer.append(s[i:j])
        i += 1

    j += 1


# -------------------------------

freq = {}
for i in pattern:
    if freq.get(i):
        freq[i] += 1
    else:
        freq[i] = 1

count = len(set(pattern))

i, j = 0, 0

while j < len(s):

    if freq.get(s[j]):
        freq[s[j]] -= 1
        if freq[s[j]] == 0:
            count -= 1

    if j - i == k:
        if count == 0:
            answer.append(s[i:j])

        if i in freq:
            if freq[i] == 0:
                count += 1
            freq[i] += 1

        i += 1

    j += 1
