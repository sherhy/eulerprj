#https://projecteuler.net/problem=54

from m054 import *

#read the file
with open("p054_poker.txt") as f:
	poker_raw = f.readlines()

#each round contains both hands
rounds = list()

breaker = 0
for line in poker_raw:
	rounds.append(line.strip())
	##DEBUGGER by count###########
	breaker +=1
	# if breaker == 7: break

#initialise
p1Count = 0
i = 0

#split to p1 hands and p2 hands
for rnd in rounds:
	i +=1
	p1, p2 = rnd.split()[:5], rnd.split()[5:]

	print(i,p1,p2)
	#compare hands and score if p1 wins
	match = compareHands(p1, p2)
	print(match)
	
	if match: p1Count +=1

	##DEBUGGER by line###############
	# bbb = input('>')
	# if bbb == 'b': break

print(p1Count)


