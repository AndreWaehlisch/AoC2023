from collections import Counter
from functools import cmp_to_key

result = 0

hands = []

cardvalues = {
	"A" : 14,
	"K" : 13,
	"Q" : 12,
	"J" : 11,
	"T" : 10,
}
for i in range(2, 9 + 1):
	cardvalues[str(i)] = i

def comparehands(x, y):
	# first check hand value
	if x[0] < y[0]:
		return -1
	elif x[0] > y[0]:
		return 1
	# else check individual cards
	else:
		for a, b in zip(x[1], y[1]):
			val1 = cardvalues[a]
			val2 = cardvalues[b]
			if val1 < val2:
				return -1
			elif val1 > val2:
				return 1
	return 0

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		cards, bid = line.split()
		cards = list(cards)
		bid = int(bid)
		c = Counter(cards)
		s = sorted(c.values())
		if s == [5]:
			value1 = 6
		elif s == [1, 4]:
			value1 = 5
		elif s == [2, 3]:
			value1 = 4
		elif s == [1, 1, 3]:
			value1 = 3
		elif s == [1, 2, 2]:
			value1 = 2
		elif s == [1, 1, 1, 2]:
			value1 = 1
		elif s == [1, 1, 1, 1, 1]:
			value1 = 0
		hands.append((value1, cards, bid))

handsorter = cmp_to_key(comparehands)
hands.sort(key=handsorter)

for rank, hand in enumerate(hands, start=1):
	result += rank * hand[-1]

print("result: ", result)
