#https://projecteuler.net/problem-56

# a, b <=100

def digitsum(n, b):
	ower = n**b
	numst = str(ower)
	signma = 0
	for i in numst:
		signma += int(i)
	return signma
	

record = 0
for i in xrange(1,101):
	for j in xrange(1,101):
		if digitsum(i,j)>record:
			record = digitsum(i,j)

print record