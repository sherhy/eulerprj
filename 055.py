#https://projecteuler.net/problem=55

#n<10000 in which n is lychel number 
#(x>=50 iterations are considered a lychel number)

def flipnumorder(n):
	numstr = str(n)
	newstr = numstr[::-1]
	return int(newstr)

def checkpalin(n):
	numstr = str(n)
	anostr = numstr[::-1]

	for i in xrange(len(numstr)/2):
		if not numstr[i] == anostr[i]: return False
	return True

def iterate(n, m):
	if not len(n) == len(m): return False
	return True

def lycheltest(n):
	# print 'checking', n
	palincounter = 49
	while palincounter>0:
		palincounter -=1
		nextiterate = n + flipnumorder(n)

		# print n,'+',flipnumorder(n),'=',nextiterate

		if checkpalin(nextiterate): 
			# print "found!"
			return False
		# print 'sum not palin, so next iteration!',palincounter,'left'
		n = nextiterate

	if palincounter == 0:
		return True


solution = 0
for i in xrange(1, 10000):
	if lycheltest(i): solution +=1

print solution