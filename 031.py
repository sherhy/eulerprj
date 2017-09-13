#coding=UTF-8
#https://projecteuler.net/problem=31

"""
200
same method for two pounds
2L
	1 	7
	2	2*6
	5	4*5
	10	11*4
	20	19*3
	50	(1+)		
1L	
50p	50		1
		20 2  19
		10 5  5
20p	20; 	1
		10^2;	11
		5^4;	4
		2 10;	10
		1		1		19
10p 	10^1; 1
		5^2;  4 
		2^5; 	5	
		1;		1		11
5p		5^1;	1	
		2^2; 	2
		1;		1		4
	!! must sort and set
2p 	2^1;	1
		1; 	1		2 
"""
#do i only have to bottom up

target = 200

s = [0]*(target+1)
s[0] = 1
coins = [1, 2, 5, 10, 20, 50, 100, 200]
for i in coins:
	for j in xrange(i, target+1):
		s[j] += s[j-i]
print s[200]
