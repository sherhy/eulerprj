#https://projecteuler.net/problem=39

#P = a+b+(a*a+b*b)**0.5

solution = dict()

for i in range(499,1,-1):
	for j in range(1,293):
		if float((i*i+j*j)**0.5).is_integer():
			prm = int((i*i+j*j)**0.5)+ i+ j
			if prm <=1000:
				try:
					solution[int(prm)]+=1
				except:
					solution[int(prm)]=0

answer = [0,0]
for x in solution:
	if solution[x] > answer[1]:
		answer = [x, solution[x]]

print answer