#p067
with open('067_triangle.txt') as f:
	prompt = f.read()

print prompt

proxy = []
for line in prompt.splitlines():
	mini = line.split()
	count = 0
	for i in mini:
		mini[count]=int(i)
		count+=1
	proxy.append(mini)
for i in proxy[::-1]:
	sum = 0
	count= 0
	for n in i: sum += int(n)
	# for n in i: 
	# 	i[count] = n-(sum/len(i))
	# 	count +=1
	print i, sum/len(i)
addline = []
for i in range(len(proxy[len(proxy)-1])):
	addline.append(0)

for i in proxy[::-1]:
	for k in range(len(i)):
		i[k]+= addline[k] 

	addline = [] 
	for p in range(len(i)-1):
		if i[p] > i[p+1]: 
			addline.append(i[p])
		else:
			addline.append(i[p+1])

print proxy

#heh feels so smarts