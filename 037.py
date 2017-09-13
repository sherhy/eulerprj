#https://projecteuler.net/problem=37

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

sieve = sieveit(2000000);

def truncate(dr, num):
	numstr = str(num)
	numlen = len(numstr)
	if numlen >1:
		if dr == 0:
			return int(numstr[1:])
		elif dr == 1:
			return int(numstr[:numlen-1])
	else:
		return num

solution = []

i = 21
while len(solution) < 11:
	i+=2
	ilen = len(str(i))
	success = True
	n = i
	for _ in xrange(ilen):
		if sieve[n]:
			n = truncate(0,n)
		else: 
			success = False

	n = i
	for _ in xrange(ilen):
		if sieve[n]:
			n = truncate(1,n)
		else:
			success = False
	if success: solution.append(i)

print solution
print sum(solution)
