import os, sys

def mrange(start, stop, step):
	while start < stop:
		yield start
		start += step

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

def sieve(n):
	isPrime = [ True ] * (n+1) # assume all are prime to start
	isPrime[0] = isPrime[1] = False # except 0 and 1, of course
	primes = [ ]
	for prime in range(n+1):
		if (isPrime[prime] == True):
			# we found a prime, so add it to our result
			primes.append(prime)
			# and mark all its multiples as not prime
			for multiple in range(2*prime, n+1, prime):
				isPrime[multiple] = False
	return primes

def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	srqt = int(n**0.5)
	f = 5
	while f <= srqt:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True 
			
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