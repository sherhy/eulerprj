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

fullcount = 10000
steve = sieve(fullcount)
print "sieved", time.time()-now,"seconds"

n = 9
found = False
while not found:
	if n > fullcount: break
	if steve[n]:
		n+=2
		continue
	found = True
	for i in xrange(1,int(n**0.5)+1):
		checkprime = n - 2*i*i
		if checkprime > 1 and steve[checkprime]:
			found = False

			print n,"=","2(",i,")^2+",checkprime

			n+=2
			break
	continue

if found:
	print "found", n

print time.time()-now, "seconds"