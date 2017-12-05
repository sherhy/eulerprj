#https://projecteuler.net/problem=61

'''
P3,n = n(n+1)/2
P4,n = n**2
P5,n = n(3n-1)/2
P6,n = n(2n-1)
P7,n = n(5n-3)/2
P8,n = n(3n-2)

the ordered set of three 4-digit numbers: 8128, 2882, 8281 has three interesting properties.
1. the set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first)
2. each polygonal type: P3,127 = 8128, P4,91 = 8281, P5,44 = 2882 is represented by a different number in the set.
3. this is the only set of 4-digit numbers with this proeperty

find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: P3-8,n is represented by a different number in the set.
'''
import time
tstart = time.time()
#whuuut, well, should start from making the sequences
global solution 
solution= []
thelist = []

def p3(n):
	gogo = n*(n+1)/2
	solution.append(gogo)
	return gogo

def p4(n):
	gogo = n**2
	solution.append(gogo)
	return gogo

def p5(n):
	gogo = n*(3*n-1)/2
	solution.append(gogo)
	return gogo

def p6(n):
	gogo = n*(2*n-1)
	solution.append(gogo)
	return gogo

def p7(n):
	gogo = n*(5*n-3)/2
	solution.append(gogo)
	return gogo

def p8(n):
	gogo = n*(3*n-2)
	solution.append(gogo)
	return gogo

#now, see if cyclic, 4-digit
#what are the args for this function tho..
#ooh, ordered set, isee, they just have to chain
def checkCyclic(setnlist):
	pass

#find minimum n and maximum n
polygonalsequence = [p3,p4,p5,p6,p7,p8]
startn = []
stopn = []
for seq in polygonalsequence:
	i = 3
	while seq(i) < 1000:
		i+=1
	startn.append(i)
	while seq(i) < 10000:
		i+=1
	stopn.append(i)
# print startn, stopn

#lingering thought is when to stop searching for the next

# #wondering whether there are any matches, since 6 cyclic set of 4-digit numbers must mean that there are duplicates
# dumplist = []
# for i in xrange(5):
# 	for q in xrange(startn[i],stopn[i]+1):
# 		dump = polygonalsequence[i](q)
# 		if dump not in dumplist:
# 			dumplist.append(dump)
# # print len(dumplist)
# #->263
# #actually this dumplist might be useful // nope

def clearlist():
	global thelist
	thelist = []

def chain(lastnumber, i):
	global solution
	if i == 5: 
		# print "success!"
		# print thelist
		return True

	numstring = str(lastnumber)
	lasttwo = numstring[-2]+numstring[-1]
	
	#there are multiple numbers starting with lasttwo as the beginning
	nextnumbers = []
	for _ in xrange(startn[i+1],stopn[i+1]):
		testnum = polygonalsequence[i+1](_)
		teststr = str(testnum)
		if teststr[:2] == lasttwo: 
			nextnumbers.append(testnum)
			# thelist.append(_)
		# solution.pop()


	if len(nextnumbers) == 0: 
		# print "bro"
		clearlist()
		return False
	
	for j in nextnumbers:
		testchain = chain(j, i+1)
		if testchain == True: return True
	clearlist()
	return False
	
clearlist()
for i in xrange(startn[0],stopn[0]+1):
	# if chain(p3,0): print "letsgooooo"
	chain(p3(i),0)

reallist =[0, p4(81),p5(64),p6(25),p7(32),p8(21)]


# for _ in xrange(startn[0],stopn[0]):
# 		testnum = polygonalsequence[0](_)
# 		teststr = str(testnum)
# 		if teststr[:2] == '65': 
# 			# print 'p3',_,":",teststr
# 			reallist[0] = int(teststr)

# print reallist
# print sum(reallist)
# #[6555, 6561, 6112, 1225, 2512, 1281]
# #24246

print time.time()-tstart,"seconds"