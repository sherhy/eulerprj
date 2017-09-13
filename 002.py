#https://projecteuler.net/problem=2

fibseries = [0,1]

i = 1
while fibseries[i]< 4000000:
	fibseries.append(fibseries[i-1]+fibseries[i])
	i+=1

solution = 0
for i in filter(lambda x: x%2==0, fibseries):
	solution+= i
print solution 