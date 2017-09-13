#https://projecteuler.net/problem=4

def checkPalindrome(num):
	string = str(num)
	for i in xrange(len(string)/2):
		if not string[i]==string[len(string)-1-i]: return False
	return True

solution = 0
for i in xrange(999,0, -1):
	for j in xrange(999,0, -1):
		if checkPalindrome(i*j) and i*j > solution: 
			solution =  i*j

print solution