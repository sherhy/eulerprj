#https://projecteuler.net/problem=60

'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and 
concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to 
produce another prime.
'''
import time, random, collections, itertools

def timer(f):
	def wrapper(*args, **kwargs):
		tini = time.time()
		res = f(*args, **kwargs)
		tfin = time.time()
		print ('{!r} {:2.2f} ms'.format(f.__name__, (tfin - tini) * 1000))
		return res
	return wrapper

def isPrime(n):
	if n == 2 or n == 3: return True
	if n < 2 or n%2 == 0: return False
	if n < 9: return True
	if n%3 == 0: return False
	srqt = int(n**0.5)
	f = 5
	while f <= srqt:
		if n%f == 0: return False
		if n%(f+2) == 0: return False
		f +=6
	return True 

def sieve(limit):
	sieve = {} 
	sieve = collections.defaultdict(lambda:True)
	sieve[0], sieve[1] = False, False
	srqt = int(limit**0.5)+1
	for n in range(4, limit+1, 2):
		sieve[n]=False
	for n in range(3, srqt, 2):
		if sieve[n]==True:
			for i in range(n*n, limit, n*2):
				sieve[i]=False
	primes = []
	for i in range(2,limit):
		if sieve[i]:
			primes.append(i)
	return primes

def concatprime(i, li):
	works = []
	for j in li:
		n = int(str(i)+str(j))
		m = int(str(j)+str(i))
		if isPrime(n) and isPrime(m):
			works.append(j)
	return works

@timer
def main():
	for a in range(len(subp)):
		for b in hm[subp[a]]:
			cs = hm[subp[a]]&hm[b]
			for c in cs:
				ds = hm[subp[a]]&hm[b]&hm[c]
				for d in ds:
					inter = hm[subp[a]]&hm[b]&hm[c]&hm[d]
					if inter:
						sols.append([subp[a],b,c,d,min(inter)])
						print(subp[a],b,c,min(inter))
	try:
		least = [sum(sols[0]),sols[0]]
		for sol in sols:
			if sum(sol) < least[0]:
				least = [sum(sol),sol]
		print(f"ans: {least}")
	except:
		print('no answer found')



def test():
	li = [3, 17, 83, 449]
	for i,j in itertools.combinations(li,2):
		n = int(str(i)+str(j))
		m = int(str(j)+str(i))
		print(f"{n}? {isPrime(n)}")
		print(f"{m}? {isPrime(m)}")

if __name__=="__main__":
	sols = []	
	limit = 10000
	subp = sieve(limit)
	hm = collections.defaultdict(set)
	for p in range(len(subp)-1):
		for j in concatprime(subp[p],subp[p+1:]):
			hm[subp[p]].add(j)

	main()
	#ans: [26033, [13, 5197, 5701, 6733, 8389]]
