#https://projecteuler.net/problem=1
solution = 0
for i in xrange(1000):
	if i % 3==0 or i%5==0: solution+=i
print solution