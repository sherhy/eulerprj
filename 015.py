#coding=UTF-8
"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""

# (2*n) th line's middlemost coefficient is the lattice count

# array path length must be the same
	# there must be 20 "D" and 20 "R"
	# same as 40 C 20 (combinatory)

n = 20
ans = 1
for i in range(1,n+1):
	ans *= (n+i)/i
print ans

# know thy math