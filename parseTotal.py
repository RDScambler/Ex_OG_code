import re

def parse_total():
	with open("group_total.txt") as f:
		header = f.readline()
		group = []
		total =[]
		for line in f:
			spline = re.split("\t", line.strip())
			group.append(spline[0].strip())
			total.append(spline[1])

		totaldic = dict(zip(group, total))
		return totaldic

parse_total()
