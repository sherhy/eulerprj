"""Special Pythagorean triplet
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc."""

# assume c is hypoteneus
# triangle property [P1:]
	# a + b > c
	# a + c > b
	# b + c > a
# right triangle [P2:]
	# a**2 + b**2 == c**2

class Trileg:
	primitives = []

	def __init__(self, x):
		self.h = x
		self.la = 1 #how to start the legs
		self.lb = x	

	def check(self):
		while True:
			fd = self.lb
		 	while (self.la + fd) > self.h and (self.la + self.h) > fd and (fd + self.h) > self.la:
		 		fd -= 1
				if (self.la**2 + fd**2) == self.h**2:
					self.lb = fd
					break
				if fd ==0: break
			if (self.la**2 + self.lb**2) == self.h**2:
				if self.lb == 0: return False
				self.add(self.la, self.lb, self.h)
				self.la +=1
				continue
				#"the pythagorean set must be primitive"
			else:
				self.la +=1
				if self.la==self.h: break

	def add(self, a,b,c):
		caseset = [a,b,c]
		caseset.sort()
		if caseset in Trileg.primitives: return False
		# for x in Trileg.primitives:
		# 	if caseset[2]%x[2] == caseset[1]%x[1] == caseset[0]%x[0]:
		# 		# print "found nonpri", caseset, "%d /" %caseset[2],"%d" %x[2], float(caseset[2]/x[2])#, float(caseset[1]/x[1])
		# 		if caseset[2]/x[2] == caseset[1]/x[1] == caseset[0]/x[0]:
		# 			return False
		Trileg.primitives.append(caseset)
		print "found pri", caseset, a+b+c
		if a+b+c ==1000:
			print "not working dude"
			print a*b*c
		return True

i = 4
while i<500:
	i+=1
	oejen = Trileg(i)
	oejen.check()

#sucked at parametrisation
#learn more maths
#see euclid's formulae

















