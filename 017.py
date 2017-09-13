#coding=UTF-8
"""
Number letter counts
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage."""

dict ={
	0: 0,
	1: 3, #one
	2: 3, #two
	3: 5, #three
	4: 4, #four
	5: 4, #five
	6: 3, #six
	7: 5, #seven
	8: 5, #eight
	9: 4, #nine
	10: 3, #ten
	11: 6,#eleven
	12: 6, #twelve
	13: 8,
	14: 8, 
	15: 7,
	16: 7,
	17: 9,#seventeen
	18: 8,#eighteen
	19: 8,#nineteen <----i had this as 9 the whole time..
	20: 6, #twenty
	30: 6,
	40: 5,
	50: 5,
	60: 5,
	70: 7,
	80: 6,
	90: 6
}

def namelength(numstr):
	global dict
	count = 0
	nums = numstr[::-1]
	if len(nums) >2: 
		if int(numstr)%100==0: count += dict[int(nums[2])]+7
		else: count += dict[int(nums[2])]+10
		
		if int(numstr)%100<21:
			count +=dict[int(numstr[1:3])]
			return count
	if len(nums) >1: 
		if int(numstr)%100 <21:
			count +=dict[int(numstr[:2])]
			return count
		count += dict[int(nums[1])*10]
	count += dict[int(nums[0])]
	return count
ans = 0
for i in range(1, 1000): #1000 not inclusive
	b = str(i)
	ans += namelength(b)
	print i, namelength(b)
ans += 11 #one thousand
print ans
