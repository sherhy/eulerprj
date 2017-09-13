#coding=UTF-8
"""Lexicographic permutations
Problem 24
A permutation is an ordered arrangement of objects. For example, 
3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, 
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"""

from mylib import factorial

permlist = list(xrange(10))

remainingperm = 1000000
solution = []
while len(permlist)>0:
	count = 0
	while remainingperm > factorial(len(permlist)-1):
		remainingperm -= factorial(len(permlist)-1)
		count+=1

	solution.append(permlist[count])
	permlist.remove(permlist[count])
	print count, solution, permlist, remainingperm

print solution