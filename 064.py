#https://projecteuler.net/problem=64
#https://en.wikipedia.org/wiki/Continued_fraction

'''
prompt:
All square roots are periodic when written as continued fractions and can be written in the form:

√N = a0 +	
1
 	a1 +	
1
 	 	a2 +	
1
 	 	 	a3 + ...

It can be seen that the sequence is repeating. For conciseness, we use the notation √23 = [4;(1,3,1,8)], to indicate that the block (1,3,1,8) repeats indefinitely.

The first ten continued fraction representations of (irrational) square roots are:

√2=[1;(2)], period=1
√3=[1;(1,2)], period=2
√5=[2;(4)], period=1
√6=[2;(2,4)], period=2
√7=[2;(1,1,1,4)], period=4
√8=[2;(1,4)], period=2
√10=[3;(6)], period=1
√11=[3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13=[3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?'''
import math

def reciprocate(n):
	if n != 0:
		return 1/n
	else:
		return 0

def splitDecimal(n):
	d1 = math.floor(n)
	rest = n-d1
	return (d1,rest)

####brute force 
def m1(n):
	i = 1
	root = n**0.5
	if root%1==0: return 0
	
	d1, rest = splitDecimal(root)
	reference = rest
	reciprocal = reciprocate(rest)

	d1, rest = splitDecimal(reciprocal)
	while not math.isclose(reference, rest):
		i +=1
		reciprocal = reciprocate(rest)
		d1, rest = splitDecimal(reciprocal)

	print(n, i)
	return i

def closeNuff(d1, d2, ep = 10**-7):
	return abs(d1 - d2) < ep

#############limitations of float-point variables
def m2(n):
	i, b = 1, []
	root = n**0.5
	if root%1==0: return 0
	
	a0, rest = splitDecimal(root)
	
	a1, rest = splitDecimal(reciprocate(rest))
	while not closeNuff(2*a0, a1):
		# print(a0, a1, closeNuff(a0,2*a1))
		i+=1
		a1, rest = splitDecimal(reciprocate(rest))
	print(n, i)
	return i%2==1

####quadratic surds
def method(n):
	root = n**0.5
	a = [math.floor(root)]
	if a[0]**2 == n: 
		return a
	f, p, q = a[0], 0, 1

	while True:
		p = f*q - p
		q = (n- p*p)//q
		f = (a[0]+p)//q
		a.append(int(f))
		if q ==1: break
	return a

if __name__ == "__main__":
	count = 0
	maxa = 10000
	for i in range(2,maxa+1):
		# print(i, len(method(i)), method(i)) 
		if (len(method(i))-1)%2==1: count +=1

	print('for N up to',maxa,":",count)