#find the maximum path sum from any node to any node

import sys

res = -sys.maxsize

def solve(root):
	global res

	if not root:
		return 0

	l = solve(root.left)
	r = solve(root.right)

	temp = max(max(l, r) + root.val, root.val)
	ans = max(temp, l + r + root.val)   # considering both cases when root in and not in answer
	res = max(ans, res)

	return temp


