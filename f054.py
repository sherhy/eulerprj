# def sorthands(line):
# 	twohands = [0,0]
# 	twohands[0]=line.split()[:5]
# 	twohands[1]=line.split()[5:]

# 	for hands in twohands:
# 		hands.sort()

# 	return twohands


# pattern = {
# 1:'high card',				#done
# 2:'one pair',					#done
# 3:'two pairs',				#done
# 4:'three of a kind',	#done
# 5:'straight',					
# 6:'flush',				 		#done
# 7:'full house',				#done
# 8:'four of a kind',	 	#done
# 9:'straight flush',		
# 10:'oooooohhhhhh royal flush'			
# }

# def samesuits(hand):
# 	hstring = ''.join(hand)
# 	for i in xrange(1,8,2):
# 		if not hstring[i] == hstring[i+2]: 
# 			return [0,1,0,0,0,0,0,0,0,0,0]
# 	return [0,1,0,0,0,0,2**6,0,0,0,0]

# def checknumbers(hand, score):
# 	hstring = ''.join(hand)
# 	cardRenum = []
# 	for i in xrange(0,10,2):
# 		if hstring[i] == "J":
# 			cardRenum.append(11)
# 		elif hstring[i] == "T":
# 			cardRenum.append(10)
# 		elif hstring[i] == "Q":
# 			cardRenum.append(12)
# 		elif hstring[i] == "K":
# 			cardRenum.append(13)
# 		elif hstring[i] == "A":
# 			cardRenum.append(1)
# 		else: 
# 			cardRenum.append(int(hstring[i]))
# 	# this gets highcard value
# 	score[1] = cardRenum

# 	checkpairs(cardRenum, score)
# 	straights(cardRenum,score)

# def straights(hand, score):
# 	cnums = sorted(hand)
# 	straight = True
# 	# mayberoyal = False
# 	if score[2]: 
# 		straight = False
# 	else:
# 		for i in xrange(4):
# 			if cnums[i] ==1:
# 				if  cnums[i+1]==2 or cnums[i+1]==10:
# 					pass
# 			elif cnums[i] == cnums[i+1]+1: 
# 				pass
# 			else:
# 				straight = False
# 	# if len(cnums) == 6:
# 	# 	straight = True
# 	# 	for i in xrange(4):
# 	# 		if not cnums[i+1] == cnums[i+2]: 
# 	# 			straight = False
# 	# 	if straight == True: mayberoyal = True
# 	if straight == True: score[5]=2**5
# 	if straight and score[6]: 
# 		score[9] = 2**9
# 		if cnums[0]==1 and cnums[4]==13: 
# 			score[10] = 1024

# def checkpairs(hand, score):
# 	# print hand,
# 	cnums = sorted(hand)
# 	pair = False
# 	triple = False
# 	doublePair = False
# 	# print cnums, 
# 	for i in range(4):
# 		this = cnums.pop()
# 		#keep the length of the list
# 		cnums.append(0)
# 		cnums.sort()
# 		# print cnums,
# 		if this == cnums[-1]:
			
# 			if pair == False:
# 				if triple and this == score[4]:
# 					#quad
# 					pair = False
# 					score[8]=this
# 				if triple:
# 					score[7] = 2**7

# 				pair = True
# 				score[2] = this
# 			elif pair:
# 				if score[2] != this:
# 					doublePair = True
# 					score[3] = this
# 				else:
# 					triple = True
# 					if doublePair: 
# 						score[7]=2**7
# 					score[4] = this	
# 					pair = False
# 				# if cnums[-2]==this:
# 	# 				triple = True
# 	# 				pair = False
# 	# 				score[4] = this
# 	# 				if cnums[-3]==this:
# 	# 					quadruple = True
# 	# 					triple = False
# 	# 					score[8] = this
# 	# 					cnums.pop()
# 	# 					cnums.append(0)
# 	# 					cnums.sort()
# 	# 				cnums.pop()
# 	# 				cnums.append(0)
# 	# 				cnums.sort()
# 	# 		if pair and score[2]!=this:
# 	# 			doublePair = True
# 	# 			score[3]= 8
# 	# 			if this > score[2]:
# 	# 				score[2] = this
				
# 	# if pair == False: score[2] = 0
# 	# if doublePair == False: score[3] = 0
# 	# if triple == False: score[4] = 0
# 	# if quadruple == False: score[8] = 0
# 	# if score[2]!=score[4]: score[7]= 2**7
		
# def comprehend(twohands):
# 	p1hand = twohands[0]
# 	p2hand = twohands[1]

# 	scorecard1 = samesuits(p1hand)
# 	scorecard2 = samesuits(p2hand)

# 	checknumbers(p1hand, scorecard1)
# 	checknumbers(p2hand, scorecard2)

# 	# print scorecard1[1:],scorecard2[1:]

# 	return [scorecard1, scorecard2]

# def comparehands(twohands):
# 	scores = comprehend(twohands)
# 	# print scores,
# 	for i in xrange(10, 0, -1):
# 		if i == 1:
# 			if 1 in scores[0][1]:
# 				scores[0][1].remove(1)
# 				scores[0][1].append(14)
# 				scores[0][1].sort()
# 			if 1 in scores[1][1]:
# 				scores[1][1].remove(1)
# 				scores[1][1].append(14)
# 				scores[1][1].sort()
# 			for k in xrange(4,-1,-1):
# 				if scores[0][1][k] == scores[1][1][k]:
# 					pass
# 				else:
# 					# print pattern[i],
# 					return scores[0][1][k]>scores[1][1][k]
# 		if scores[0][i] == scores[1][i]: 
# 			pass
# 		else: 
# 			g.write (pattern[i],)
# 			# print scores[0][i] > scores[1][i]
# 			return scores[0][i] > scores[1][i]