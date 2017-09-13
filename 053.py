#https://projecteuler.net/problem=53


def factori(start, end=None):
	if start == 0:
		return 1
	if start == end:
		return end
	if start == 1:
		return 1
	if end == None:
		end = 1
	return start*factori(start -1, end)

def combinations(n,r):
	#n!/(r!(n-r)!)
	# if r > n-r:
	# 	r = n-r
	return factori(n)/(factori(r)*factori(n-r))

sol = 0
for i in xrange(23,101):
	for j in xrange(1,i+1):
		if combinations(i,j) > 1000000:
			sol +=1
print sol

#i have to undrstand why sol changes when i xrange(__ , 101)
#is changed from 1 to 22, which shouln't make a difference, 
# according to the prompt