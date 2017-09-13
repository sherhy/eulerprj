#https://proejcteuler.net/problem=62

#the cube, 41063625 (345)^3 can be permuted to produce two other cubes: 56623104 (384)^3 and 66430125 (406)^3. in fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

#find the smallest cube fow which exactly five permutations of its digits are cube
import time
tstart = time.time()
def permutate(firstn, secondn):
	firststr = str(firstn)
	numlist = []
	for i in firststr:
		numlist.append(i)

	secondstr = str(secondn)
	for i in secondstr:
		if i in numlist: 
			numlist.remove(i)
		else:
			return False

	if len(numlist) ==0:
		return True
	else:
		return False

# print permutate(41063625,66430125)
for abra in xrange(2,11):
	n = 10
	while n**3<(10**abra):
		n+=1
	atrt = n

	while n**3<10**(abra+2):
		n+=1
	limit = n+1


	# skiplist = []
	for i in xrange(atrt,limit):
		count = 0
		a = i**3
		for j in xrange(i,limit):
			# if j not in skiplist:
			b = j**3
			if permutate(a,b): count +=1
		if count >= 5:
			print i
			break

print time.time()-tstart, "seconds"
#5027
#89.6927399635 seconds
