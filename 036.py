#httpts://projecteuler.net/problem=36
"""
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def returnbin(num):
	return int(bin(num)[2:])

def checkpalindrome(num):
	digits = str(num)
	strlen = len(digits)
	for i in xrange(strlen/2):
		if not int(digits[i])==int(digits[strlen-1-i]): return False
	return True

def checkboth(num):
	if checkpalindrome(num) and checkpalindrome(returnbin(num)): return True
	else: return False

solution = 0
for i in xrange(1000000):
	if checkboth(i): 
		print i, bin(i)
		solution +=i

print solution
