#https://projecteuler.net/problem=57

#first iteration
n = 0

# i=0 numberator; i=1 denominator
ab = [2,1]

sol = 0

def flipandadd(ab):
	global sol, n
	n += 1
	cd = [ab[0]+ab[1], ab[0]]

	if len(str(cd[0]))>len(str(cd[1])): sol +=1
	print cd 
	if n == 1000:
		return False
	else:
		return nextiteration(cd)

def nextiteration(ab):
	return [ab[0]+ab[1],ab[1]]

while True:
	ab = flipandadd(ab)
	if ab:
		continue
	else:
		break

print sol, n
