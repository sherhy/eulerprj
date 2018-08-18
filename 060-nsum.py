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

def check(a, s, d, n):
	x = pow(a, d, n)
	if x == 1: return True
	for i in range(s - 1):
		if x == n - 1: return True
		x = pow(x, 2, n)
	return x == n - 1
def miller_rabin(n, k=10):
	if n == 1 or (not n): return False
	if n == 2: return True
	s ,d = 0, n - 1
	while d % 2 == 0:
		d >>= 1
		s += 1
	for i in range(k):
		a = random.randrange(2, n - 1)
		if not check(a, s, d, n): return False
	return True

@timer
def sieve(limit):
	sieve = {} 
	sieve = collections.defaultdict(lambda:True,sieve)
	sieve[0], sieve[1] = False, False
	srqt = int(limit**0.5)+1
	for n in range(4, limit+1, 2):
		sieve[n]=False
	for n in range(3, srqt, 2):
		if sieve[n]==True:
			for i in range(n*n, limit, n*2): #the crucial cuttime
				sieve[i]=False
	primes = []
	for i in range(2,limit):
		if sieve[i]:
			primes.append(i)
	return primes

@timer
def nsum(li: list, n: int, target:int) -> list:
	#i'm afraid this is going to go out of hand unless memoized
	if n == 2:
		groups = []
		for i in range(len(li)-1):
			j = len(li)-1
			while i < j:
				summ = li[i]+li[j]
				if summ == target: 
					groups.append([li[i],li[j]])
					j-=1
				elif summ < target: break
				else: j -=1
		return groups
	else:
		res = []
		for i in range(len(li)-n+1):
			groups = nsum(li=li[i+1:],n= n-1, target=target-li[i])
			if groups == []: continue
			for g in groups:
				g.append(li[i])
			for g in groups:
				if g not in res:
					res.append(g)
		return res

alreadyfalse = list()
def concatprime(li):
	for i, j in itertools.combinations(li, r=2):
		n = int(str(i)+str(j))
		m = int(str(j)+str(i))
		if not (miller_rabin(n) and miller_rabin(m)):
			pair = set([i,j])
			alreadyfalse.append(pair)
			return False
	return True


@timer
def main():
	limit = 10000
	subp = sieve(limit)
	size = 4
	count = 0
	print(f"length: {len(subp)}\n")
	for a,b,c,d in itertools.combinations(subp, r=size):
		count +=1
		false = False
		li = [a,b,c,d]
		# if count % 10000 == 0: print(count, li)
		for x,y in itertools.combinations(li, r=2):
			pair = set([x,y])
			if pair in alreadyfalse:
				false = True
				break
		if false: continue
		if concatprime([a,b,c,d]): 
			print([a,b,c,d])
			return True
	return 1

#i also had an algorithm that finds n elements adding to k, thinking i only had to check primes
#found solution for n=4 in 2.5sec

@timer
def test():
	kwargs = {
		'li': [3,7,109],
	}
	print(concatprime(**kwargs))

if __name__=="__main__":
	main()
	# test()