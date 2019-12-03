import glob
import re

to_parse = glob.glob("*.txt")
output = open("group_data.txt", "w")
groupname = "Group"
headers = output.write(f"{groupname.ljust(18)}\t{'EOGs'}\t{'Gene families'}\n")	# Formatted headers using .ljust (pads loose space up to the value of argument).

def parse_OG(file):								# Function designed to parse OG stats as found in output .txt files
	with open(file) as f:
		for line in f:
			og = re.search(r"\w*:\s(\w*)", line)			# I.e. "Shared gene families: NNNN"
			if og:
				fname = name[0].ljust(18)			# Formats spacing as with the headers.
				outputWrite = output.write(f"{fname}\t{og.group(1)}")

for file in to_parse:
	name = re.split("_", file)
	if name[0] == name[1]:
		parse_OG(file)
		with open("group_total.txt") as fr:
			for line in fr:
				spline = re.split("\t", line.strip())
				spline1 = spline[0].strip()			# Stripping excess whitespace from string (so it is equal to name[0]).
				if name[0] == spline1:				# Adds total OG data to next column of corresponding group.
					outputWrite = output.write(f"\t\t{spline[1]}\n")	# Formatted for neatness.




output.close()


