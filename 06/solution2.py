import re
from tqdm import tqdm

result = 1

time = None

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if time is None:
			time = int(''.join(re.findall("\d+", line)))
		else:
			distrecord = int(''.join(re.findall("\d+", line)))

num = 0
for tcharge in tqdm(range(1, time+1)):
	tmove = time - tcharge
	mydist = tmove * tcharge
	if mydist > distrecord:
		num += 1
if num > 0:
	result *= num

print("result: ", result)
