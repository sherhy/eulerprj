#https://projecteuler.net/problem=63

def check(base, n):
	global count
	exp = str(base**n)
	print exp
	if len(exp)==n:
		count += 1
		print count, "count"
		return True
	elif len(exp)>n:
		return False
	else:
		return True

count = 0
l = 1000
for n in xrange(1,l):
	for base in xrange(1,l):
		if not check(base, n):
			break

print count