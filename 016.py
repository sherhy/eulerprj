#coding=UTF-8

"""Power digit sum
Problem 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?"""

longnum = str(1 << 1000)
ans = 0
for digit in longnum:
	ans += int(digit)
print ans