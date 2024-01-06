import re

result = 1

times = None

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if times is None:
			times = list(map(int, re.findall("\d+", line)))
		else:
			dists = list(map(int, re.findall("\d+", line)))

for time, distrecord in zip(times, dists):
	num = 0
	for tcharge in range(1, time+1):
		tmove = time - tcharge
		mydist = tmove * tcharge
		if mydist > distrecord:
			num += 1
	if num > 0:
		result *= num

print("result: ", result)
