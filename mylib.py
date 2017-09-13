import os, sys

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

from math import sqrt
def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

#miller rabin primarity test
from random import randrange
def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1: return True
		for i in xrange(s - 1):
			if x == n - 1: return True
			x = pow(x, 2, n)
		return x == n - 1
def miller_rabin(n, k=10):
	if n == 2: return True
	if not n & 1: return False
	s = 0
	d = n - 1
	while d % 2 == 0:
		d >>= 1
		s += 1
	for i in xrange(k):
		a = randrange(2, n - 1)
		if not check(a, s, d, n): return False
	return True

#makes a default dictionary of primes
from collections import defaultdict
def sieveit(limit):
	sieve = {} 
	sieve = defaultdict(lambda:True,sieve)
	sieve[0], sieve[1] = False, False
	srqt = int(limit**0.5)+1
	for n in xrange(4, limit+1, 2):
		sieve[n]=False
	for n in xrange(3, srqt, 2):
		if sieve[n]==True:
			for i in range(n*n, limit, n*2): #the crucial cuttime
				sieve[i]=False
	return sieve
	
# dont know when i'd use this one
# def sumofproperdivisors(n):
# 	limit = int(n**0.5)+1
# 	divisors = [1]
# 	for i in range(2, limit):
# 		if n%i==0:
# 			divisors.append(i)
# 			if (n/i) not in divisors:
# 				divisors.append((n/i))
# 	x= 0
# 	for k in divisors:
# 		x += k
# 	return x

def factorial(n):
	if n ==1 or n ==0: return 1
	else:
		return n*factorial(n-1)