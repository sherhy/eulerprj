#https://projecteuler.net/problem=38

def checkpandigital(intst):
	digits = set()
	for i in range(1,10):
		digits.add(str(i))
	if len(intst) == 9 and digits == set(intst): 
		return True
	else: 
		return False

solution = 0

i = 9
while i < 10000:
	testst = str(i)
	n =2
	go = True
	while go:
		testst = testst + str(i*n)
		n+=1
		if len(testst)>=9: go = False
	if checkpandigital(testst): 
		if int(testst) > solution: solution = int(testst)
	i+=1

print solution