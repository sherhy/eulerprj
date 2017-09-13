#https://projecteuler.net/problem=32

def ispandigital(multiplicand, multiplier):
	product = multiplier*multiplicand
	digits = str(multiplicand)+str(multiplier)+str(product)
	digitset = set()
	for i in digits:
		if i =="0" or i in digitset: return False
		digitset.add(i)
	if len(digitset) == 9: 
		return product
	else: return False
solution = set()
digitarray = ['1','2','3','4','5','6','7','8','9']
for i in xrange(9):
	digitarray.sort()
	l = digitarray[i]
	digitarray.remove(l)
	for j in xrange(8):
		digitarray.sort()
		m = digitarray[j]
		digitarray.remove(m)
		for c in xrange(7):
			digitarray.sort()
			n = digitarray[c]
			digitarray.remove(n)
			for d in xrange(6):
				digitarray.sort()
				o = digitarray[d]
				digitarray.remove(o)
				for e in xrange(5):
					digitarray.sort()
					p = digitarray[e]
					digitarray.remove(p)

					firstnumber = int(l)
					secondnumber = int(m+n+o+p)
					if ispandigital(firstnumber, secondnumber):
						solution.add(ispandigital(firstnumber, secondnumber))
					firstnumber = int(l+m)
					secondnumber = int(n+o+p)
					if ispandigital(firstnumber, secondnumber):
						solution.add(ispandigital(firstnumber, secondnumber))
					
					digitarray.append(p)
				digitarray.append(o)
			digitarray.append(n)
		digitarray.append(m)
	digitarray.append(l)

print sum(solution)
