#https://projecteuler.net/problem=44
import time

starttime = time.time()
#make a lot of pentagon numbers
pentarray = set()
for i in xrange(1,6001):
	pentarray.add(int(i*(3*i-1)*0.5))

#iterate through the combinations
import itertools
solution = 0
for x in itertools.combinations(pentarray, 2):
	d = x[1]-x[0]
	if x[1]+x[0] not in pentarray: continue
	if d  not in pentarray: continue
	if solution == 0:
		solution = d
		print x
		break

print solution

print time.time()-starttime, "seconds"