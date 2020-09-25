
def nth_fibonacci_recur(n):
    if n == 0 or n == 1:
        return n
    
    return nth_fibonacci_recur(n - 1) + nth_fibonacci_recur(n - 2)


def nth_fibonacci_dp(n):
    fib = [0] * ( n + 1 )
    fib[0] = 0
    if n > 0:
        fib[1] = 1

    for i in range(2, n + 1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]


print(nth_fibonacci_recur(9))

print(nth_fibonacci_dp(9))