#!/usr/local/bin/python3
#project euler problem 66
#https://projecteuler.net/problem=66

#Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

import math

def printit(f):
	def wrapper(*args, **kwargs):
		print(f(*args,**kwargs))
	return wrapper

def pells(x,y,d):
	return x*x - d*y*y == 1


def isSquare(n):
	sqr = math.sqrt(n)
	if sqr.is_integer(): return True
	return False

#9*9 - 5*4*4 = 1

# @printit
def solve(d):
	global sols
	if isSquare(d): 
		return 0
	# for x in range(1000): #dont know upper limit
	x,y = d,0
	while y*y*d < x*x:
		y+=1
		x = math.sqrt(d*y*y+1)

		if pells(int(x),y,d): 
			print(d,x,y)
			return int(x)

if __name__=="__main__":
	sols = dict()
	limit = 1000
	for i in range(2,limit+1):
		sols[i]=solve(i)
	values = sols.values()
	# print(sols)
	print(max(values))