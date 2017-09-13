#coding=UTF-8
"""Names scores
Problem 22
Using names.txt (right click and 'Save Link/Target As...'), 
a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. Then working out the alphabetical 
value for each name, multiply this value by its alphabetical position in the 
list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?"""

def nameval(name):
	sum = 0
	for char in name:
		sum += ord(char)-64
	return sum

with open('022_names.txt') as f:
	prompt = f.read()
proxy =prompt.split('","')
proxy[0]=proxy[0].split('"')[1]
proxy[len(proxy)-1]=proxy[len(proxy)-1].split('"')[0]
proxy.sort()

count = 0
total = 0
for name in proxy:
	count +=1
	total += (nameval(name)*count)

print total