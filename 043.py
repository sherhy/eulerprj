#https://projecteuler.net/problem=43

import itertools

solution = 0

for i in itertools.permutations(range(10)):
	digits = ''
	for j in i:	
		digits += str(j)
	if int(digits[1:4]) % 2 != 0: continue
	if int(digits[2:5]) % 3 != 0: continue
	if int(digits[3:6]) % 5 != 0: continue
	if int(digits[4:7]) % 7 != 0: continue
	if int(digits[5:8]) % 11 != 0: continue
	if int(digits[6:9]) % 13 != 0: continue
	if int(digits[7:11]) % 17 != 0: continue
	solution += int(digits)

print solution

#16695334890