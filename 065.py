#problem=65
'''
https://projecteuler.net/problem=65
Hence the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...
What is most surprising is that the important mathematical constant,
e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''
import math
class Number:
	def __init__(self,val:float = 0.0):
		self.val = val
		self.chain = []
		self.fracpart = []

	def __str__(self):
		return f"{self.val}"

	def reciprocate(self):
		self.val = 1/self.val

	def next(self):
		i = self.val//1
		self.chain.append(int(i))
		self.val = self.val - i
		self.fracpart.append(self.val)

		boollist = [closenuff(self.val, i) for i in self.fracpart[:-1]]
		if any(boollist) and len(self.fracpart)>2:
			ind = [i for i, x in enumerate(boollist) if x][0]
			print(f"there's repetition!\t{self.chain[ind+1:]}")
			# self.chain = f"{self.chain[:ind+1]};{self.chain[ind+1:]}"
			return False
		self.reciprocate()

class Fraction(Number):
	def __init__(self, n, d):
		super().__init__(float(n)/d)
		self.n = n
		self.d = d		

	def __add__(self, other):
		top = self.n* other.d + self.d*other.n
		bot = self.d*other.d
		return Fraction(n=top, d=bot)

	def simplify(self, li=[]):
		factors = [
			factorize(self.n),
			factorize(self.d)
		]

		for i in factors[0][::-1]:
			if i in factors[1]:
				factors[0].remove(i)
				factors[1].remove(i)
		top, bot = 1, 1
		for i in factors[0]:
			top = top * i
		for j in factors[1]:
			bot = bot * j

		# print(factors)
		
		# self.n = top
		# self.d = bot
		return Fraction(top,bot)

	def reciprocate(self):
		self.n, self.d = self.d, self.n

	def __repr__(self):
		return f"{self.n}/{self.d}"
	def __str__(self):
		return f"{self.n}/{self.d}"

def makecf(li=[1, 2, 2, 2, 2, 2, 2]):
	fchain=[]
	for i in range(len(li)-1,0,-1):
		cf = Fraction(n=li[i],d=1)		
		for j in li[i-1::-1]:
			cf.reciprocate()
			# print(cf, i, j)

			cf = Fraction(n=j,d=1) + cf
		fchain.append(cf)
	#last one at li[0]
	fchain.append(Fraction(n=li[0],d=1))
	#fchain.reverse()
	# print(fchain)
	return fchain

def closenuff(a,b,epsilon=1.e-7):		
	if abs(a-b)<epsilon: return True
	return False

def factorize(n, li=None):
	if li == None:
		li = []
	for i in range(2,int(math.sqrt(n))+1):
		if n%i ==0:
			li.append(i)
			return factorize(n/i, li)
	li.append(int(n))
	return li


def solve():
	# val = float(input("val: "))
	val = math.e
	print(val)
	f = Number(val=val)
	while f.val > 1 and len(f.chain)<100:
		if f.next(): break
	chain = makecf(f.chain)

	lastf = chain[-1].simplify()
	# print(chain[-1])
	print(lastf)
	sol = 0
	for i in str(lastf.n):
		sol += int(i)
	print(sol)

def main():
	val = math.e
	print(val)
	fchain = [2]
	count = 1
	while len(fchain)<100:
		fchain.append(1)
		fchain.append(count*2)
		fchain.append(1)
		count +=1
	chain = makecf(fchain)
	print(len(chain))
	# lastf = chain[0].simplify()
	lastf = chain[0]
	print(lastf)

	sol = 0
	for i in str(lastf.n):
		sol += int(i)
	print(sol)

if __name__ =="__main__":
	main()