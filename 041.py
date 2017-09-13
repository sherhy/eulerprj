#https://projecteuler.net/problem=41
import time
start_time = time.time()

def checkpandigital(intst):
	digits = set()
	n = len(intst)
	for i in range(1,n+1):
		digits.add(str(i))
	if n == len(set(intst)): 
		return True
	else: 
		return False

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

sieve = sieveit(9000000)

print("--- %s seconds ---" % (time.time() - start_time))