numberdict = {
	'A': 14,
	'2': 2,
	'3': 3,
	'4': 4,
	'5': 5,
	'6': 6,
	'7': 7,
	'8': 8,
	'9': 9,
	'T': 10,
	'J': 11,
	'Q': 12,
	'K': 13
}

def RoyalF(hand):
	#true or false
	return Flush(hand) and Royal(hand)

def StraightF(hand):
	#returns high card
	if Flush(hand):
		return Straight(hand)
	else:
		return 0

def FourKind(hand):
	numbers = sorted([numberdict[card[0]] for card in hand])
	#count the number of repetitions in hand
	for i in numbers:
		if numbers.count(i) == 4: return i
	return 0

def Fullhouse(hand):
	numbers = sorted([numberdict[card[0]] for card in hand])
	#remove pairs from copied list
	original = list(numbers)
	highcard = ThreeKind(hand) if ThreeKind(hand) else OnePair(hand)
	for i in numbers:
		if numbers.count(i) == 2:
			original.remove(i)
		elif numbers.count(i) ==3:
			original.remove(i)
	
	if len(original) == 0:
		return highcard
	else:
		return 0

def Flush(hand):
	# suit mathing
	suit = hand[0][1]
	for card in hand:
		if suit != card[1]: return False
	return True

def Straight(hand):
	#count down from highcard card
	highcard = HighCard(hand)
	#get card numbers
	numbers = sorted([numberdict[card[0]] for card in hand])
	
	if numbers == list(range(highcard-4,highcard+1)):
		return highcard

	# for 'wheel' hand
	elif numbers == [2,3,4,5,14]:
		return 5
	else:
		return 0

def ThreeKind(hand):
	#same idea as FourKind
	numbers = sorted([numberdict[card[0]] for card in hand])

	for i in numbers:
		if numbers.count(i) == 3: return i
	return 0

def TwoPair(hand):
	numbers = sorted([numberdict[card[0]] for card in hand])
	#remove pairs from copied list
	original = list(numbers)
	highcard = 0
	for i in numbers:
		if numbers.count(i) == 2:
			original.remove(i)
			if i>highcard: highcard = i
	
	if len(original) == 1:
		return highcard
	else:
		return 0

def OnePair(hand):
	numbers = sorted([numberdict[card[0]] for card in hand])

	for i in numbers:
		if numbers.count(i) == 2: return i
	return 0

def HighCard(hand):
	#return highcard as int
	highcard = 0
	for card in hand:
		highcard = numberdict[card[0]] if numberdict[card[0]] > highcard else highcard
		# print(highcard)
	return highcard


########################
def Royal(hand):
	#s if hand is royal
	royalset = ('T','J','K','Q','A')
	cards = []
	for card in hand:
		cards.append(card[0])
	return royalset == set(cards)


#method container
def compareHands(p1, p2):
	#return True if p1 wins
	h1 , h2 = RoyalF(p1),RoyalF(p2)
	if h1 or h2:
		print(RoyalF.__name__,end=" ")
		if not h1 and h2: #this way, program moves on to the next evaluation
			return h1 and (not h2) #most likely not both having RSF

	h1, h2 = StraightF(p1), StraightF(p2)
	if h1 or h2:
		print(StraightF.__name__,end=" ") 
		if h1 != h2:
			return h1 > h2 

	h1, h2 = FourKind(p1), FourKind(p2)
	if h1 or h2:
		print(FourKind.__name__,end=" ") 
		return h1 > h2 #there is a clear winner

	h1, h2 = Fullhouse(p1), Fullhouse(p2)
	if h1 or h2:
		print(Fullhouse.__name__,end=" ")
		if not h1 == h2:
			return h1 > h2 #otherwise move on

	h1, h2 = Flush(p1), Flush(p2)
	if h1 or h2:
		print(Flush.__name__,end=" ")
		if h1 and h2:
			return HighCard(p1) > HighCard(p2)
		return h1 and (not h2) #this makes a clear winner

	h1, h2 = Straight(p1), Straight(p2)
	if h1 or h2:
		print(Straight.__name__,end=" ")
		if h1 != h2:
			return h1 > h2 

	h1, h2 = ThreeKind(p1), ThreeKind(p2)
	if h1 or h2:
		print(ThreeKind.__name__,end=" ")
		if h1 != h2:
			return h1 > h2

	h1, h2 = TwoPair(p1), TwoPair(p2)
	if h1 or h2:
		print(TwoPair.__name__,end=" ")
		if h1 != h2:
			return h1 > h2

	h1, h2 = OnePair(p1), OnePair(p2)
	if h1 or h2:
		print(OnePair.__name__,end=" ")
		if h1 != h2:
			return h1 > h2

	else:
		print(HighCard.__name__,end=" ")
		return HighCard(p1) > HighCard(p2)
