from mylib import checkprime 

count = 0
i = 1
while not count == 10001:
	i+=2
	if checkprime(i): count +=1
print count, i