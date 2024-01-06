result = 0

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		numbers = line.split(":")[1]
		sides = numbers.split("|")
		winning = [int(i) for i in sides[0].split()]
		mynums = [int(i) for i in sides[1].split()]
		score = 0
		for num in mynums:
			if num in winning:
				if score == 0:
					score = 1
				else:
					score *= 2
		result += score

print("result: ", result)
