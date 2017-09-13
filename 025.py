#coding=UTF-8
"""The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 
1000 digits?"""

fib = [1,1]
i = 2
while True:
	i +=1
	print i
	c = len(fib)
	n = fib[c-1] + fib[c-2]
	if len(str(n)) <1000:
		fib.append(n)
	else:
		print n
		break
