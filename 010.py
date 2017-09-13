"""Summation of primes
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million."""
limit = 2000000
solution = 0

primli = [2, 3, 5, 7, 11, 13]
i = 13
while i < limit:
	i +=2
	if i%2==0 or i%3==0 or i%5==0 or i%7==0 or i%11==0 or i%13==0: continue
	for x in primli:
		# print i, x, i%x
		if i%x==0: break	
	if i%x!=0: 
		print i
		primli.append(i)


# i=2
# sequence = range(2,limit+1)
# while i <= limit:
# 	if i in sequence:
# 		n = 2
# 		while n*i < limit:
# 		# for n in range(2,limit):
# 			if n*i in sequence:
# 				sequence.remove(n*i)
# 				print i,": not ", n*i
# 			n +=1
# 	i+=1

for i in primli:
	
	solution += i
print solution

#soooooo slow