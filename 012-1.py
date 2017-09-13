# coding=utf-8
from primes import * #primelist

t =1
a= 1
cnt = 0
while cnt <501:
	cnt =1
	a +=1
	t +=a
	tt = t
	for i in range(len(primelist)):
		if primelist[i]**2 > tt:
			cnt *= 2
			break

		exponent = 1
		while tt%primelist[i]==0:
			exponent+=1
			tt = tt/primelist[i]

		if exponent >1: cnt *=exponent
		if tt ==1: break

print t