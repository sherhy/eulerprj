#https://projecteuler.net/problem=60

'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''

#shake off the shmame from looking up the answer in problem51; it was about time: move on

'''
- find primes (no problem)
- check through the prime set
	- match_making
		- concatenating
- find next iteration
'''

# class Set(object):
# 	def __init__(self):
# 		self.set = []

#if the example gives the lowest four pair, then maybe finding the fifth guy is fastest? -> but that's not the art of it
import time
tstart = time.time()
from random import randrange
def check(a, s, d, n):
		x = pow(a, d, n)
		if x == 1: return True
		for i in xrange(s - 1):
			if x == n - 1: return True
			x = pow(x, 2, n)
		return x == n - 1
def miller_rabin(n, k=10):
	if n == 1: return False
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

#
def matchMake(primelist):
	# print "started matchmaking"
	listlen = len(primelist)
	for i in xrange(listlen-2,-1,-1):
		for j in xrange(listlen-1, i, -1):
			bloop = concatenate(primelist[i],primelist[j])
			if bloop == False: return False
	# print sum(primelist), primelist
	return True


def concatenate(a, b):
	astr = str(a)
	bstr = str(b)
	test1 = int(astr+bstr)
	test2 = int(bstr+astr)
	# print test1, test2
	if miller_rabin(test1) and miller_rabin(test2): 
		return True
	else:
		# print "concat fail"
		return False

# testlist = [3,7,109,673]
# print matchMake(testlist)
# okay, it works, now, how to form the next testlist if matchMake returns False

# testlist = [3,7,109,673]
# limit = 10000
# for _ in xrange(5, limit, 2):
# 	if miller_rabin(_) and _ not in testlist:
# 		trylist = [3,7,109,673, _]
# 		if matchMake(trylist): break
# print sum(trylist) 


def incrementprime(prime):
	prime +=2
	while True:
		if not miller_rabin(prime): prime +=2
		else: return prime

def findworkigset(trylist, start = 0):
	tstart = time.time()
	if len(trylist)==5: return [True,trylist]
	prime1 = trylist[-1]+2
	if start != 0: prime1 = start+2
	while True:
		testlist = trylist + [prime1]
		nextterm = matchMake(testlist)
		prime1 = incrementprime(prime1)
		if nextterm == True: break
		#if time.time()-tstart > 2: 
		if prime1 >= 126253:
			print "couldn't find one", trylist
			return [False,trylist]
	return findworkigset(testlist)

# findworkigset([3])
# findworkigset([7])
# 989809 [7, 9, 19, 433, 989341]
# findworkigset([9])
# print findworkigset([7,9],19)[1]

experiment = findworkigset([53])
ind3 =0
ind2 =0
ind1 =0

while True:
	if experiment[0]: 
		print "found",sum(experiment[1]), experiment[1]
		if raw_input('cont?> ') == 'y': 
			experiment = findworkigset(experiment[1][:2],experiment[1][2])
			continue
		else: break
	
	try:
		i = 3
		ind3 +=1
		if ind3 ==3:
			ind3 = 0
			ind2 +=1
			i = 2
		if ind2 ==5:
			ind2 = 0
			ind1 +=1
			i = 1
		if ind1 ==5:
			ind1 = 0
			nextnumber = incrementprime(experiment[1][0])
			if nextnumber ==5: nextnumber = 7
			experiment = findworkigset([nextnumber])
			continue
		experiment = findworkigset(experiment[1][:i],experiment[1][i])
	except:
		experiment = findworkigset(experiment[1][:len(experiment[1])-1],experiment[1][len(experiment[1])-1])
# 177115 [7, 9, 19, 1237, 175843]
# 332257 [7, 9, 127, 136027, 196087]
# 253153 [13, 21, 523, 1129, 251467]
# 126253 [9, 19, 2791, 29671, 93763]
# 516043 [9, 37, 1237, 93763, 420997]
# 330973 [3, 31, 4159, 17209, 309571]

print time.time()-tstart, "sec"
#laststopcouldn't find one [53, 113, 23027]
#found 100969 [79, 399, 5659, 8461, 86371]
#cont?> n
#284.445734978 sec
