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
			for a, b in zip(seeds[::2], seeds[1::2]):
				sa = int(a)
				sb = int(b)
				result[range(a, a+b)] = (a, False)
		elif ":" in line:
			for k,v  in result:
				newv = v
				newv[1] = False
				result[k] = newv
		elif theline[0].isnumeric():
			startDest, startSource, n  = map(int, line.split())
			for k, v in result.items():
				raise NotImplementedError("TODO")

print("result: ", min(result.values()))
