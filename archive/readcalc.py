import re

with open("group_data.txt") as f:
	header = f.readline()
	for line in f:
		fields = re.split("\t", line.strip())
		proportion = round(int(fields[1]) / int(fields[2]) * 100, 2)		# Calculates proportion of exclusive OGs, rounds to 2 d.p.s.
		print(fields[0].strip().ljust(20) + " % unique OGs:\t", proportion)
