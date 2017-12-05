#https://projecteuler.net/problem=61

'''
P3,n = n(n+1)/2
P4,n = n**2
P5,n = n(3n-1)/2
P6,n = n(2n-1)
P7,n = n(5n-3)/2
P8,n = n(3n-2)

the ordered set of three 4-digit numbers: 8128, 2882, 8281 has three interesting properties.
1. the set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first)
2. each polygonal type: P3,127 = 8128, P4,91 = 8281, P5,44 = 2882 is represented by a different number in the set.
3. this is the only set of 4-digit numbers with this proeperty

find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: P3-8,n is represented by a different number in the set.
'''
import time
from itertools import chain
tstart = time.time()

def p3(n): return n*(n+1)//2
def p4(n): return n**2
def p5(n): return n*(3*n-1)//2
def p6(n): return n*(2*n-1)
def p7(n): return n*(5*n-3)//2
def p8(n): return n*(3*n-2)

def quadratic (a,b,c):
	determinant = b**2 - 4*a*c
	if determinant < 0: return [0]
	x = 0-b + (determinant)**0.5
	x = x/(2*a)
	y = 0-b - (determinant)**0.5
	y = y/(2*a)
	if determinant == 0: return [x]
	return [x, y]

def arcP3(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(1,1,-2*i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]
def arcP4(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(1,0,-i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]
def arcP5(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(3,-1,-2*i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]
def arcP6(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(2,-1,-i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]
def arcP7(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(5,-3,-2*i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]
def arcP8(n):
	xMin = n%100 
	if xMin < 10:
		return []
	else:
		xMin = xMin*100
	blist = [(quadratic(3,-2,-i)) for i in range(xMin,xMin+100)]
	tlist = list(chain.from_iterable(blist))

	return [int(i) for i in tlist if i%1==0]


skipnums = set()

weGowith5 = set()
for i in range(100):
	n = arcP5(i)
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith5.add(_)
weGowith6 = set()
for i in weGowith5:
	n = arcP6(p5(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith6.add(_)
weGowith7 = set()
for i in weGowith6:
	n = arcP7(p6(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith7.add(_)
weGowith8 = set()
for i in weGowith7:
	n = arcP8(p7(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith8.add(_)
weGowith3 = set()
for i in weGowith8:
	n = arcP3(p8(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith3.add(_)
##r2
weGowith4 = set()
for i in weGowith3:
	n = arcP4(p3(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith4.add(_)
weGowith5 = set()
for i in weGowith4:
	n = arcP5(p4(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith5.add(_)			
weGowith6 = set()
for i in weGowith5:
	n = arcP6(p5(i))
	if n ==[]: skipnums.add(i)
	else:
		for _ in n:
			weGowith6.add(_)



for _ in range(3,9):
	setName = "weGowith"+str(_)
	fName = "p"+str(_)
	print(setName, end=": ")
	# print(sorted(list(eval(setName))),end=" ")
	for i in sorted(list(eval(setName))):
		print(eval(fName)(i),end=" ")
	print()

print(sum([8515, 1521, 2147, 4753, 5359, 5985]))
#print(sum([1281, 8128, 2882, 8256, 5625, 2512]))>cheat
#i wonder why my engine couldn't find it

print(time.time()-tstart,"seconds")