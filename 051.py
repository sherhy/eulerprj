#https://projecteuler.net/problem=51
import time
tnow = time.time()

#i gave up and looked up http://www.mathblog.dk/project-euler-51-eight-prime-family/

#more like i started working on this problem 2 months ago..

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

def makenum(numberlist):
		newnum = ""
		for i in numberlist:
			newnum = newnum+i
		altnum = int(newnum)
		return altnum

def checknthdigit(num, nlist):
	#digits counting from 1s place
	numlis = list()
	numstr = str(num)
	primefam = list()
	numindex = len(numstr)

	for d in numstr:
		numlis.append(d)

	#i have to change a number's x location with xrange(10)
	for _ in xrange(10):
	
		for m in nlist:
			numlis[numindex-m] = str(_)

		altnum = makenum(numlis)
		if miller_rabin(altnum): 
			primefam.append(altnum)
	return primefam

def isthisayes(num):
	numstring = str(num)
	nonolist = ("0","2","4","5",'6','8')
	if numstring[len(numstring)-1] in nonolist: 
		return False
	else:
		return True

"""#---------------------------------------------------------------
#it's like, when doing the checking, it removes other candidates
notcandidate = []

#don't have to count up.. just form the numbers n-digit based

#now need a method to count up

1* 10 -> ones digit place will never give more than 5 primes
*1 1

1** 100 -> anything that has to do with ones place doesn't work
10* 10
1*1 -> even with these cases, numbers that end with 0,2,4,5,6,8 are 
			 never primes

10*0
1*00
1**0

100*0
10*00
1*000
1*0*0
10**0
1**00
1***0
--
1000*0
100*00
10*000
1*0000

100**0
10*0*0
1*00*0
10**00
1*0*00
1**000

10***0
1*0**0
1***00
1**0*0

1****0
"""

# limit = 1000000
# li = [2,3,5]
# counter = 0
# solutions = []


# for _ in xrange(limit/10,limit):
# 	if isthisayes(_): 
	

# 			#how to get rid of duplicate searching



# 		result = checknthdigit(_, li)
# 		if len(result) > 6 :
# 			if result not in solutions:
# 				solutions.append(result)
# 				print _, "primefam:", result

#_----------___----___---__--___--__-___--__-different approach, get a prime list, and look within that

# limit = 10000000
# data = []

# for i in xrange(100, limit):
# 	if isthisayes(i) and miller_rabin(i):
# 		data.append(i)

# print len(data)

# f = open("newfile.txt", "w")

# for stuff in data:
# 	f.write(str(stuff)+" ")

# f.close()
def checkwithindata(_,nlist):
	global data
	numlis = list()
	numstr = str(_)
	primefam = list()
	numindex = len(numstr)-1
	for d in numstr:
		numlis.append(d)
	for p in xrange(10):
	
		for m in nlist:
			numlis[m] = str(p)

		altnum = makenum(numlis)
		if miller_rabin(altnum): 
			primefam.append(altnum)
	return primefam


with open("p051_junkprime.txt") as f:
	data = f.read()
data = data.split(" ")
beta = []
for i in data:
	try:
		beta.append(int(i))
	except:
		continue
data = beta

solutions = []
li = [6]
'''
* all clear
1**000
1***00
'''
digitlength = 6
for i in data: 
	if i < 10**(digitlength-1):
		continue
	if i >= 10**digitlength:
		break
	result = checkwithindata(i, li)
	if len(result) > 6 :
		if result not in solutions:
			solutions.append(result)
			print "primefam:", result

"""
10000*0
1000*00
100*000
10*0000
1*00000
1**0000
1*0*000
1*00*00
1*000*0
10**000
10*0*00
10*00*0
100**00
100*0*0
1000**0
1***000
1**0*00
1**00*0
1*0**00
1*0*0*0
1*00**0
10***00
10**0*0
10*0**0
100***0
10****0
1*0***0
1**0**0
1***0*0
1****00

"""
#primefam: [4004509, 4114519, 4224529, 4444549, 4554559, 4774579, 4884589, 4994599]
#primefam: [2090021, 2191121, 2292221, 2494421, 2595521, 2696621, 2898821, 2999921]

print time.time()-tnow, "seconds"