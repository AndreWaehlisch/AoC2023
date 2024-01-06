from collections import defaultdict

result = defaultdict(lambda : 0)

with open("input", "r") as file:
	for theline in file:
		line = theline.rstrip()
		split1 = line.split(":")
		cardID = int(split1[0][5:])
		result[cardID] += 1
		numbers = split1[1]
		sides = numbers.split("|")
		winning = [int(i) for i in sides[0].split()]
		mynums = [int(i) for i in sides[1].split()]
		wins = 0
		for num in mynums:
			if num in winning:
				wins += 1
		for add in range(cardID + 1, cardID + 1 + wins):
			result[add] += result[cardID]

print("result: ", sum(result.values()))
