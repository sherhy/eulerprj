#coding=UTF-8
"""Amicable numbers
Problem 21
Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair 
and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 
44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 
1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000."""

def sumofproperdivisors(n):
	limit = int(n**0.5)+1
	divisors = [1]
	for i in range(2, limit):
		if n%i==0:
			divisors.append(i)
			if (n/i) not in divisors:
				divisors.append((n/i))
	x= 0
	for k in divisors:
		x += k
	return x

i = 1
cik = {}
while i <10000:
	cik[i] = checkn(i)
	i+=1

i =2
sum = 0
while i <10000:
	if checkn(checkn(i)) == i:
		if not checkn(i) == i:
			sum += i
	i+=1

print sum