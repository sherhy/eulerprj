#https://projecteuler.net/problem=34

def factorial(num):
	if num < 2:
		return 1
	else:
		return num*factorial(num-1)

def checkcurious(num):
	digits = str(num)
	curiosity = 0
	for i in digits:
		curiosity += factorial(int(i))
	# print 'num', num, 'curiosity', curiosity
	if curiosity == num: return True


"""
how to reduce unnecessary iterations?
	digits like 8, 9 are too big

what is the upper limit?


"""
solution = 0
for i in xrange(10,100000):
	if checkcurious(i): 
		print ":)"
		solution += i
print solution