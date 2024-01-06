import re

result = 0

lines = []

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		lines.append(list(line))

atnum = False
curnum = ''

def check(i, j):
	global curnum, atnum, result
	atnum = False
	# check around last num
	l = len(curnum)
	a = max(j - l - 1, 0)
	b = j + 1
	symbolsearch = lines[i][a:b] + lines[max(0, i-1)][a:b] + lines[min(len(lines)-1, i+1)][a:b]
	m = re.search("[^0-9\.]", ''.join(symbolsearch))
	if m:
		result += int(curnum)
	curnum = ''

for i, iline in enumerate(lines):
	for j, jchar in enumerate(iline):
		if jchar.isdigit(): # digit
			curnum += jchar
			atnum = True
		elif atnum: # not digit
			check(i, j)
	if atnum:
		check(i, j)

print("result: ", result)
