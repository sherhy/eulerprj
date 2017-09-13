"""Smallest multiple
Problem 5
Published on Friday, 30th November 2001, 06:00 pm; Solved by 326744; Difficulty rating: 5%
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?"""

#biggest exponential covers the lower exponentials
##6 will be deleted if case like 2^2,3^2
#prime factorization

rangel = 20

primes = []
factori = {}

def pake(n):
	po = range(1, n+1)
	for i in po:
		primch(i)
	primes.reverse()
	for i in primes:
		factori[i] = 0

def primch(n):
	if n>1:
		for i in range(2,n):
			if n%i==0:
				return False
		else:
			primes.append(n)
			return True
	else:
		return False

pake(rangel)
solution = {}
ppap = {}
for x in factori:
	solution[x]=factori[x]
"""
1. list of primes
2. greatest common multiple -->prime factorization
3. division or products and gcm = lcm
"""
def resetppap():
	for x in factori:
		ppap[x]=factori[x]
def factorize(n):
	for i in primes:
		if n%i ==0:
			quot = n/i
			ppap[i] += 1
			factorize(quot)
			break

def comp(pap):
	for x in pap:
		if pap[x] > solution[x]: 
			solution[x]=pap[x]

for i in range(1,rangel+1):			
	resetppap()
	factorize(i)
	comp(ppap)

lcm =1
for i in solution:
	l = i**solution[i]
	lcm *= l

print lcm

"""or make prime class"""