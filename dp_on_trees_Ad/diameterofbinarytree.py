# find the maximum distance from one leaf node to another leaf node

import sys
res = -sys.maxsize

def solve(root):
	global res
	
	if not root:
		return 0


	l = solve(root.left, res)
	r = solve(root.right, res)

	temp = max(l, r) + 1
	ans = l + r + 1
	res = max(ans, res)

	return temp

def main():

	solve(root)
	return res
