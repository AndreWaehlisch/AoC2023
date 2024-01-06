import re

result = 0

lines = []

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		lines.append(list(line))

for i, iline in enumerate(lines):
	for j, jchar in enumerate(iline):
		if jchar == "*":
			gearlist = []
			for theline in [iline, lines[i-1], lines[i+1]]: # first and last line dont have a "*"
				for m in re.finditer("\d+", ''.join(theline)):
					if (j <= m.end()) and (j >= m.start() - 1):
						gearlist.append(int(m.group()))
			if len(gearlist) == 2:
				result += gearlist[0] * gearlist[1]

print("result: ", result)
