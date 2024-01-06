import re, collections

result = {}

lines = None

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		if lines is None:
			lines = []
			split = line.split(":")
			seeds = split[1].split()
			for seed in seeds:
				s = int(seed)
				result[s] = s
		elif ":" in line:
			swapped = collections.defaultdict(lambda : False)
		elif theline[0].isnumeric():
			startDest, startSource, n  = map(int, line.split())
			for k, v in result.items():
				if (v in range(startSource, startSource + n)) and (not swapped[k]):
					result[k] = (v - startSource) + startDest
					swapped[k] = True

print("result: ", min(result.values()))
