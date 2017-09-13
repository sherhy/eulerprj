#https://projecteuler.net/problem=40

champerownesConstant = "."
n = 190000
for i in xrange(1,n):
	champerownesConstant = champerownesConstant + str(i)

solution = 1
for i in range(7):
	solution *= int(champerownesConstant[10**i])
print solution