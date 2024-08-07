import numpy as np

with open("input", "r") as file:
	result = 0
	for i, theline in enumerate(file):
		line = theline.rstrip()
		numlist = list(map(int, line.split()))
		difflists = [numlist, ]
		nums = numlist
		while True:
			diff = np.diff(nums)
			if np.all(diff == 0):
				break
			difflists.append(diff)
			nums = diff
		for i, diff in enumerate(reversed(difflists), start=2):
			if i > len(difflists):
				break
			difflists[-i] = np.append(difflists[-i], difflists[-i][-1] + diff[-1])
		result += difflists[0][-1]
	print("result:", result)
