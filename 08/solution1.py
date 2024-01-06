from itertools import cycle

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

current_place = "AAA"
for i, direction in enumerate(cycle(path), start=1):
	map_entry = mymap[current_place]
	current_place = map_entry[direction == "R"] # use left or right path
	if current_place == "ZZZ":
		print("result: ", i)
		break
