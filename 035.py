#https://projecteuler.net/problem=35
def checkprime(n):
	if n ==1: return False
	elif n < 4: return True
	elif n%2==0: return False
	elif n<9: return True
	elif n%3==0: return False
	else:
		limit = int(n**0.5)
		i = 5
		while i < limit:
			if n%i == 0:
				return False
			elif n%(i+2) == 0:
				return False
			i+=2
		return True
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

sieve = sieveit(1000000)

def checkcircular (num):
	if sieve[num]:
		digitstring = str(i)
		if len(digitstring) > 1:
			shift = digitstring[1:len(digitstring)]+digitstring[0]
			while not shift == digitstring:
				if sieve[int(shift)]:
					shift = shift[1:len(digitstring)]+shift[0]
					continue
				else: return False
			return True
		else:
			return True
	else:
		return False


count = 1
for i in xrange(1, 1000000, 2):
	if checkcircular(i): count +=1
print count