#https://projecteuler.net/problem=58

import time
tnow = time.time()

from random import randrange
def miller_rabin(n, k=10):
	if n == 2: return True
	if not n & 1: False
	def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1: return True
		for i in xrange(s - 1):
			if x == n - 1: return True
			x = pow(x, 2, n)
		return x == n - 1
	s = 0
	d = n - 1
	while d % 2 == 0:
		d >>= 1
		s += 1
	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n): return False
	return True

p, m = 3.0 , 5.0
n = 3

while True:
	n += 2
	# if n*n > limit: 
	# 	print "overlimit"
	# 	break
	for k in xrange(1,4):
		if miller_rabin(n*n-k*(n-1)): p +=1
	m += 4
	if p/m < 0.1: break
print p/m ,n

print time.time()-tnow, "seconds"