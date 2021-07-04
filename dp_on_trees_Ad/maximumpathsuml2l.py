# find the maximum path sum from leaf to leaf

import sys

res = -sys.maxsize


def solve(root):
    global res
    if not root:
        return 0

    l = solve(root.left)
    r = solve(root.right)

    temp = max(l, r) + root.val

    # considering both cases when root constitutes the answer and when not
    ans = max(temp, l + r + root.val)

    res = max(res, ans)

    return temp
