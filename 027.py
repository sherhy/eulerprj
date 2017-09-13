#coding=UTF-8
#https://projecteuler.net/problem=27

from collections import defaultdict
limit = 2000000
sieve = {} 
sieve = defaultdict(lambda:True,sieve)
srqt = int(limit**0.5)+1
for n in xrange(4, limit+1, 2):
	sieve[n]=False
for n in xrange(3, srqt, 2):
	if sieve[n]==True:
		for i in xrange(n*n, limit, n*2): sieve[i]=False

print sieve[11171]
maxcount = 0

def f1(a,b):
	global sieve
	global maxcount
	n = 0
	while True:
		if (n*n)+(n*a)+b > 0 and sieve[(n*n)+(n*a)+b]: 
			n +=1
		else: break
	if n > maxcount:
		maxcount = n
		solution = a*b
		print "new solution:", solution, a, b, maxcount

for i in xrange(-998,1000):
	for j in xrange(-1000, 1001):
		if sieve[j]:f1(i,j)
