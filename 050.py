#https://projecteuler.net/problem=50

#consecutive primes that add up to a prime

import collections

def sieve(high):
	global primes
	primes = collections.defaultdict(lambda: True) #<- careful of this
	primes[0], primes[1] = False, False
	sqrt = int(high**0.5)+1
	for i in xrange(4,high,2):
		primes[i]=False
	for i in xrange(3,sqrt,2):
		if primes[i]:
			for j in xrange(i*i, high, 2*i):
				primes[j]=False

primelimit = 1000000
sieve(primelimit)
# primelist=[2]
# for i in xrange(3,primelimit, 2):
# 	if primes[i]: primelist.append(i)


sumlimit = 1000000
consecprimes = []
recordlen = 0
solution = 0
thingseq = [2]
for i in xrange(3, int(sumlimit/2), 2):
	thingseq.append(i)
	for j in xrange(i+2, int(sumlimit/2), 2):
		if primes[j]:
			thingseq.append(j)
			if sum(thingseq)>sumlimit: break
			if primes[sum(thingseq)]:
				if len(thingseq)>recordlen:
					recordlen = len(thingseq)
					solution = sum(thingseq)
					consecprimes = thingseq
	thingseq = []


print solution, recordlen


