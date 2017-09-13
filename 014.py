#coding=UTF-8
#https://projecteuler.net/problem=14

def collatssequence (n):
	if n%2 ==0:
		return n/2
	else:
		return 3*n+1

colution = 0
for i in xrange(13,1000001):
	print i
	count = 0
	testnum = i
	while not collatssequence(testnum) == 1:
		testnum = collatssequence(testnum)
		count +=1
	if count > colution:
		colution = count
		solution = i

print solution
