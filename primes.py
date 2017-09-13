primelist = []
with open('65500primes.txt') as f:
	for prime in f:
		primelist.append(int(prime.rstrip(' \t\r\n\0')))