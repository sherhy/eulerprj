#coding=UTF-8
"""Non-abundant sums
Problem 23
A perfect number is a number for which the sum of its proper divisors is 
exactly equal to the number. For example, the sum of the proper divisors of 28 
would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n 
and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number 
that can be written as the sum of two abundant numbers is 24. By mathematical 
analysis, it can be shown that all integers greater than 28123 can be written as 
the sum of two abundant numbers. However, this upper limit cannot be reduced any 
further by analysis even though it is known that the greatest number that cannot 
be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of 
two abundant numbers."""

from mylib import sumofproperdivisors

limit = 28123
abunds = []
for i in range(1,limit):
	# if i == sumofproperdivisors(i):
	# 	print i, "---------------perfect"
	if i < sumofproperdivisors(i):
		abunds.append(i)

# # gets rid of all 12+6n
# f = 0
# marktoremove=[]
# for i in range(len(abunds)-1):
# 	if abunds[i] == 12+6*f:
# 		marktoremove.append(abunds[i])
# 		f+=1
# for i in marktoremove:
# 	abunds.remove(i)

print len(abunds)





"""[12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, 96, 100, 
102, 104, 108, 112, 114, 120, 126, 132, 138, 140, 144, 150, 156, 160, 162, 168, 174, 176, 180, 186, 192, 196, 198, 200, 
204, 208, 210, 216, 220, 222, 224, 228, 234, 240, 246, 252, 258, 260, 264, 270, 272, 276, 280, 282, 288, 294, 300, 
304, 306, 308, 312, 318, 320, 324, 330, 336, 340, 342, 348, 350, 352, 354, 360, 364, 366, 368, 372, 378, 380, 384, 390, 392, 396, 400, 
402, 408, 414, 416, 420, 426, 432, 438, 440, 444, 448, 450, 456, 460, 462, 464, 468, 474, 476, 480, 486, 490, 492, 498]"""

# # 무식
# long = []
# repeat = []
# for i in abunds:
# 	print i
# 	n = 1
# 	while True:
# 		p = (i+12)+6*n
# 		if p>limit:
# 			break
# 		if p not in long:
# 			long.append(p)
# 		else:
# 			# print "optimse", p
# 			repeat.append(p)
# 		n+=1

# # 무식
# for n in range(len(abunds)-1):
# 	poss = []
# 	for i in range(len(abunds)-n):
# 		c = abunds[n]+abunds[n+i]
# 		poss.append(c)
# 		if c not in long:
# 			long.append(c)
# 		else: 
# 			print "optimse", c, "--", abunds[n], "+",abunds[n+i]

