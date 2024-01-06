import re

l = []

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		m = re.findall("\d", line)
		l.append(int(m[0]+m[-1]))

print(sum(l))
