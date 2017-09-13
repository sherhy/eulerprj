#https://projecteuler.net/problem=42

#read the file and make into word list
#BUT every word has quotations
with open("p042_words.txt") as file:
	data = file.read().split(",")

tiangleiteration = list()
for n in range(1,50):
	tiangleiteration.append(int(0.5*n*(n+1)))

alphabetdic = {}
alphacount = 1
for i in xrange(97, 123):
	alphabetdic[chr(i).upper()]= alphacount
	alphacount += 1

def checkTriangle(word):
	wordval = 0
	for i in word:
		wordval += alphabetdic[i]
	if wordval in tiangleiteration: 
		return True
	else:
		return False

solution = 0
for i in data:
	word = i[1:-1]
	if checkTriangle( word ): solution +=1

print solution
