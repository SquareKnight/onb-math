"""Lattice paths
m;Grid width;int;20`n;Grid height;int;20
#Grid   #Pascal's Triangle
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""


def attempt_1(m, n):
	grid = []
	grid.append(list([1]*(n+1)))
	for i in range(1, m+1):
		grid.append([])
		row = grid[i]
		row.append(1)
		for j in range(1, n+1):
			row.append(grid[i-1][j] + row[j-1])

	return grid.pop().pop()


def attempt_2(m, n):
	row = [1] * (n+1)

	for i in range(m):
		for j in range(1, n+1):
			row[j] = row[j] + row[j-1]

	return row.pop()


import math
def attempt_3(m, n):
	return math.factorial(m+n) // (math.factorial(m) * math.factorial(n))


def run(m, n):
	#return attempt_1(m, n)
	#return attempt_2(m, n)
	return attempt_3(m, n)


if __name__ == '__main__':
	print(run(3, 3))
