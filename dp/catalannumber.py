
def catalan_recur(n):

    if n <= 0:
        return 1

    s = 0
    for i in range(0, n):
        s += catalan_recur(i) * catalan_recur(n - i - 1)

    return s


def catalan_dp(n):
    if n in [0, 1]:
        return 1
        
    catalan = [1] * (n + 1)
    catalan[0], catalan[1] = 1, 1

    for i in range(2, n + 1):
        catalan[i] = 0
        for j in range(i):
            catalan[i] += catalan[j] * catalan[i - j - 1]

    return catalan[n]


for i in range(10): print(catalan_recur(i))
print("----")
for i in range(10): print(catalan_dp(i))