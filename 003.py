#https://projecteuler.net/problem=3

from mylib import sieveit

number = 600851475143
sieve = sieveit(int(number**0.5))

primelist = []
for i in xrange(int(number**0.5)):
	if sieve[i]: primelist.append(i)

solution =0
while not number == 1:
	for i in primelist:
		if not number % i:
			number /= i
			if i > solution: solution = i
			continue
print solution