"""quesiton 6:
sum of squares, arithmetic sum difference """

def sum(x):
	a = range(1,x+1)
	s = 0
	for i in a:
		s += i
	return s
	# this is too dumb n(1st + last)/2

hun = sum(100)**2

def sqrange(x):
	a = range(1, x+1)
	s = 0
	for i in a:
		s += i**2
	return s
	# there is a formula for this too: 
	#This gives f(n) = (1/6)(2n^3 + 3n^2 +n) = n(1/6)(2n + 1)(n + 1).

print hun-sqrange(100)
