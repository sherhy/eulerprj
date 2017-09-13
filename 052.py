#https://projecteuler.net/problem=52

def checkfoo(n1, n2):
	numm1 = []
	num1 = str(n1)
	num2 = str(n2)
	if len(num1) < len(num2): return False
	for i in num1:
		numm1.append(i)	
	for j in num2:
		if j in numm1:
			numm1.remove(j)
	if numm1 == []: return True
	else: return False

solnotfound = True
i = 1
while solnotfound:
	docont = True
	i += 1
	for j in range(1,7):
		if not checkfoo(i, i*j):
			docont = False
			break
	if not docont: continue
	else: solnotfound = False

print i
