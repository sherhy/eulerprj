#https://projecteuler.net/problem=49
'''increases by x each term
a(1) is four digit
a(3) is also four digit
a1,a2,a3 uses same digts'''
import itertools, collections

def seieve(limit):
	ddd = collections.defaultdict(lambda: True, a = {})
	ddd[0], ddd[1] = False, False
	sqrt = int(limit**0.5)+1
	for n in xrange(4, limit, 2):
		ddd[n] = False
	for n in xrange(3, sqrt, 2):
		if ddd[n] ==True:
			for m in xrange(n*n, limit, n*2):
				ddd[m] = False
	return ddd

def conc(num):
	nu = ''
	for i in range(4):
		nu = nu + str(num[i])
	return int(nu)

sieve = seieve(9999)

possidigits= []
for i in xrange(1001,10000, 2):
	if sieve[i]:
		possidigits.append(i)
# print len(possidigits) 

def nused(num):
	sst = str(num)
	intlist = []
	for i in sst:
		intlist.append(i)
	tst = ''
	intlist.sort()
	for i in intlist:
		tst = tst + i
	return int(tst)

defdigits = collections.defaultdict(lambda: [], ds= {})
for i in possidigits:
	defdigits[nused(i)].append(i)

for i in xrange(1,10000,2):
	if len(defdigits[i]) > 2:
		# print i, defdigits[i]
		checkp = defdigits[i]
		while len(checkp)>2:
			d = 0
			c = 0
			for tries in xrange(len(checkp)-(d+2)):
				c+=1
				nextnum = 2*checkp[c] - checkp[d]
				if nextnum in checkp:
					print i, "lolllllllllll", checkp[0], checkp[c], nextnum
			checkp = checkp[1:]

#find groups of numbers that use same digits
#make a list
#perform search algorithm

# digits = [1,2,3,4,5,6,7,8,9,0]
# perms = itertools.permutations(digits,4)
# possidigits = []
# for i in perms:
# 	check = conc(i)
# 	if sieve[check] and check>1000:
# 		possidigits.append(i)
# #print len(possidigits), possidigits[0]
# #len = 510

# combs = itertools.combinations(digits,4)
# possicomb = []


# for i in combs:
# 	possicomb.append(i)

# 	checkp = []
# 	for perms in possidigits:
# 		conti = True
# 		perm = str(perms)
# 		for digits in perm:
# 			if digits not in i:
# 				conti = False
# 				break
# 		if conti:
# 			checkp.append(conc(perms))

# 	if len(checkp)<3: continue
# 	print i, checkp	

# 	checkp.sort()
# 	while len(checkp)>2:
# 		d = 0
# 		c = 0
# 		for tries in xrange(len(checkp)-(d+2)):
# 			c+=1
#			nextnum = 2*checkp[c] - checkp[d]
#			if nextnum in checkp:
#				print i, "lolllllllllll", checkp[0], checkp[c], nextnum
# 		checkp = checkp[1:]
