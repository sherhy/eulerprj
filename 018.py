# coding=UTF-8
"""
Maximum path sum I
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)"""

prompt = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# for line in prompt.splitlines():
# 	count += 1
# 	nth = line.split()
# 	if count ==1: 
# 		sum +=int(nth[n]) 
# 		continue
# 	if nth[n]>nth[n+1]:
# 		sum += int(nth[n])
# 	else:
# 		sum += int(nth[n+1])
# 		n +=1
# print sum			this only finds the directly larger terms

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



