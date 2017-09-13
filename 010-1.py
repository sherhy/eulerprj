# for large numbers, xrange will throw an error.
# OverflowError: Python int too large to convert to C long
# to get over this:

def mrange(start, stop, step):
    while start < stop:
        yield start
        start += step

# benchmarked on an old single-core system with 2GB RAM.

from math import sqrt

def is_prime(num):
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in mrange(3, int(sqrt(num)) + 1, 2))

# benchmark is_prime(100**10-1) using mrange
# 10000 calls, 53191 per second.
# 60006 function calls in 0.190 seconds.

limit =2000000
primli = []
solution = 0
for i in range(2, limit):
	if is_prime(i):
		print i
		primli.append(i)
for i in primli:
	solution += i
print solution