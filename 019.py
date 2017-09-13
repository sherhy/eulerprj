"""Counting Sundays
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?"""

year = 1900
month = {
	'jan': 3,
	'feb': 0,
	'mar': 3,
	'apr': 2,
	'may': 3,
	'jun': 2,
	'jul': 3,
	'aug': 3,
	'sep': 2,
	'oct': 3,
	'nov': 2,
	'dec': 3
}
counter = 0
currentday = 0

while year <2001:
	if year%4==0 and (year%100!=0 or year%400==0): month['feb'] =1
	else: month['feb']=0

	for days in month:
		currentday = (month[days] + currentday)%7
		if currentday ==6: counter +=1

	year +=1

print counter