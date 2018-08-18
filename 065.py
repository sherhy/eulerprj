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
class Fraction:
	def __init__(self,val:float):
		# self.n = num
		# self.d = den
		# self.val = num/den
		self.val = val
		self.chain = []

	def __str__(self):
		return f"{self.chain}"
	def reciprocate(self):
		# self.n, self.d = self.d, self.n
		self.val = 1/self.val

	def simplify(self):
		pass

	def next(self):
		# i = self.n//self.d
		i = self.val//1
		self.chain.append(int(i))
		self.val -= i
		self.reciprocate()
		if i in self.chain:
			ind = self.chain.index(i)
			print(f"reapeating {self.chain[ind:]}")
			return 0
		# self.n -= self.d*i
		


def solve():
	# num, den = [float(i) for i in input("frac: ").split('/')]
	val = float(input("val: "))
	f = Fraction(val)
	# while f.n > f.d and f.n != 0:
	while f.val > 1:
		try: 
			if f.next() == 0: break
		except ZeroDivisionError:
			break

	print(f)


if __name__ =="__main__":
	solve()