# exec(open("solution1.py").read())
import numpy as np

def hash(x):
	result = 0
	for i in x:
		asc = ord(i)
		result += asc
		result *= 17
		result %= 256
	return result

with open("input", "r") as file:
	for i, theline in enumerate(file):
		line = theline.rstrip()
		splitlist = line.split(",")
		result = 0
		for i in splitlist:
			result += hash(i)
	print("result:", result)
