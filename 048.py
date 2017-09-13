#https://projecteuler.net/problem=48

def selfpower(n):
	num = n**n
	lastdigits = str(num)[::-1][:10][::-1]
	return int(lastdigits)

sol = 0
for i in xrange(1,1001):
	sol += selfpower(i)

print str(sol)[::-1][:10][::-1]