#https://projecteuler.net/problem=26

def divide(dividend, divisor, count, remainders):
	count += 1
	if dividend >= divisor:
		check = dividend%divisor
		if not check == 0:
			if check in remainders:
				count -=1
				return [divisor, count]
			else:
				remainders.add(check)
				check*=10
				return divide(check, divisor, count, remainders)
		else:
			return [divisor, count]
	else:
		dividend *= 10
		remainders.add(dividend)
		return divide(dividend, divisor, count, remainders)

best = 0
for i in xrange(1,1001):
	current = divide(1,i,-1, set())
	if current[1] > best:
		best = current[1]
print best