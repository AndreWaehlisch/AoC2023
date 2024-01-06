import re

l = []

d = {
	"one" : 1,
	"two" : 2,
	"three" : 3,
	"four" : 4,
	"five" : 5,
	"six" : 6,
	"seven" : 7,
	"eight" : 8,
	"nine" : 9,
}

pattern1 = "\d"
pattern2 = "\d" # oneight is valid for "one" AND "eight", so check reversed strings as well
for i in d:
	pattern1 += "|" + i
	pattern2 += "|" + i[::-1]

def c(x, reverse=False):
	try:
		if reverse:
			return str(d[x[::-1]])
		else:
			return str(d[x])
	except (KeyError, TypeError):
		return x

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		m1 = re.findall(pattern1, line)
		a = c(m1[0])
		m2 = re.findall(pattern2, line[::-1])
		b = c(m2[0], True)
		l.append(int(a + b))

print(sum(l))
