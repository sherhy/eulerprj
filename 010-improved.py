limit = 2000000
srqt = int(limit**0.5)+1

from collections import defaultdict
sieve = {} 
sieve = defaultdict(lambda:True,sieve)

for n in range(4, limit+1, 2):
	sieve[n]=False

for n in range(3, srqt, 2):
	if sieve[n]==True:
		# print n
		for i in range(n**2, limit, n*2): #the crucial cuttime
			sieve[i]=False

# solution = 0
# for i in range(2,limit+1):
# 	if sieve[i]:
# 		solution += i

# print solution


#fucking fast
