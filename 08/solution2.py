from itertools import cycle
from tqdm import tqdm

path = None
mymap = {}

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if path is None:
			path = line
		elif len(line) > 1:
			key, values = line.split("=")
			val1, val2 = values.split(",")
			mymap[key.strip()] = (val1.strip()[1:], val2.strip()[:-1])

current_places = []
for key in mymap:
	if key[-1] == "A":
		current_places.append(key)

raise NotImplementedError
