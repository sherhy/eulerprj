#https://projecteuler.net/problem=46
import time
now = time.time()

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

from collections import defaultdict
def sieve(nmax):
	steve ={}
	steve = defaultdict(lambda: True, steve)
	steve[0], steve[1] = False, False
	sqrt = int(nmax**0.5)+1
	for i in mrange(4,nmax+1,2):
		steve[i]=False
	for j in mrange(3, sqrt, 2):
		if steve[j]==True:
			for k in mrange(j*j, nmax, j*2):
				steve[k]= False
	return steve

fullcount = 100000000
steve = sieve(fullcount)
print "sieved", time.time()-now,"seconds"


contthis = True
current = 50000001
while contthis:
	if current % 100000==1:
		print current
	if steve[current]: 
		current +=2
		continue	
	else:
		n = 1
		contthis = False
		while n**2 < current:
			checkprime = current - 2*n*n
			if steve[checkprime]:
				# print "current:",current,"checkprime",checkprime,steve[checkprime] 
				contthis = True
				break
			else :
				n+=1
		current += 2
		if current > fullcount:
			contthis = False

if not contthis:
	print "found,", current

print time.time()-now, "seconds"