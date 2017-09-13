#https://projecteuler.net/problem=47

def primefactorise (num):
	# i dont know whether chunking is faster 
	# or setting the top limit to the root of the set number
	pass

def chunk(num):
	factors = {}
	top = num
	while True:
		for i in xrange(2,top+1):
			if top%i ==0:
				if i in factors:
					factors[i] +=1
				else:
					factors[i] = 1
				break
		top = top/i
		if top ==1: break
	return factors

targetfre = 4
n = 102000
solution = []
while True:
	# if n % 1000 == 0 : print n
	if len(chunk(n)) == targetfre:
		solution.append(n)
	else:
		solution = []
	n+=1
	if len(solution) == targetfre: break

print solution

# answer took quite some time