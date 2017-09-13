#https://projecteuler.net/problem=33

def checkex(numerator, denominator):
	n = str(numerator)
	d = str(denominator)
	furthercheck = False
	for i in n:
		if i in d and not i == "0":
			furthercheck=True
			n = n.replace(i,"")
			d = d.replace(i,"")
	if n =="" or d == "" or float(d)==0: return [1]*2
	if furthercheck and float(numerator)/denominator == float(n)/float(d):
		return [numerator, denominator]
	else: return [1]*2

solution = [1]*2
for i in xrange(10,100):
	for j in xrange(i,100):
		mult =  checkex(i, j)
		solution[0] *= mult[0]
		solution[1] *= mult[1]

def simplify(arr):
	for i in xrange(2,arr[0]):
		if arr[0]%i==0 and arr[1]%i==0:
			arr[0]/=i
			arr[1]/=i
			return arr
	return False

while simplify(solution):
	solution = simplify(solution)

print solution