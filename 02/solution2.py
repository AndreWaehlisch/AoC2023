import re

result = 0

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		m1 = re.fullmatch("Game (\d+): (.+)", line)
		mgroups = m1.groups()
		gamestr = mgroups[1]
		mblue = re.findall("(\d+?) blue", gamestr)
		blues = max([int(i) for i in mblue]) if len(mblue) > 0 else 0
		mred = re.findall("(\d+?) red", gamestr)
		reds = max([int(i) for i in mred]) if len(mred) > 0 else 0
		mgreen = re.findall("(\d+?) green", gamestr)
		greens = max([int(i) for i in mgreen]) if len(mgreen) > 0 else 0
		result += blues * reds * greens

print("result: ", result)
