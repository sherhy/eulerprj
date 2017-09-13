#https://projecteuler.net/problem=41
import time, itertools
start_time = time.time()

from math import sqrt
def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

n = 10
conti = True
while conti:
#make panditigal
	pans = []
	for i in itertools.permutations(range(1,n)):
		digits = ''
		for j in i:	
			digits += str(j)
		if int(digits[n-2]) % 2 ==1: pans.append(int(digits))

	npans = pans[-1::-1]

	for i in npans:
		if is_prime(i):
			print i
			conti = False
			break
	n -=1

print("--- %s seconds ---" % (time.time() - start_time))