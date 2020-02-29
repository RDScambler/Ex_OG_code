import re			# *** tabledic.py outputs the same genome proportion data as table2.py, but stores it in dictionaries - easier to read. ***
import group
import glob
import parseTotal

group_names = group.groups()
group_names.sort()						# Alphabetical order important since output files in directory are ordered alphabetically.
totalOG = parseTotal.parse_total()
output = open("prop_data.txt", "w")

for name in group_names:
	data = []
	total = totalOG[name]					# Accesses total values.
	to_parse = glob.glob("*.txt")
	for file in to_parse:
		filename = file.split("_")
		if name in filename:
			with open(file) as f:
				for line in f:
					og = re.search(r"\w*:\s(\w*)", line)					# Extracts number of shared OGs.
					if og:
						prop = round(int(og.group(1)) / int(total) * 100, 2)		# Converts into % of each group's genome.
						data.append(prop)						# Shared % of each group is stored in data.

	propdic = dict(zip(group_names, data))
	print(propdic)
	outputWrite = output.write(f"{name}\t{str(propdic)}\n")

output.close()

