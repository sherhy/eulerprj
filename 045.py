#https://projecteuler.net/problem=45
import time

starttime = time.time()

notfound = True
hn = 144
pn = 0
tn = 0
# need to make separately running lists...
# count up H, and count up the rest until it catches up,
# keep the n-iteration count

current = 0
def hUp():
	global hn
	hn += 1
	return hn*(hn*2-1)

def pUp():
	global pn
	pn += 1
	return pn*(pn*3-1)*0.5

def tUp():
	global tn
	tn += 1
	return tn*(tn+1)*0.5

while notfound:
	current = hUp()
	tnum = tUp()
	pnum = pUp()
	while tnum < current: 
		tnum = tUp()
	while pnum < current: 
		pnum = pUp()
	if current == tnum and pnum == tnum: notfound = False

print "H", hn, "P", pn, "T", tn, "num", current
print starttime-time.time()