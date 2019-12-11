import re			# *** table2.py extracts the same data as table.py, but converts the pairwise OGs to % total for each group. ***
import group
import glob
import parseTotal

group_names = group.groups()
group_names.sort()
data = []

for name in group_names:
	to_parse = glob.glob("*.txt")
	for file in to_parse:
		filename = file.split("_")
		if name in filename:
			with open(file) as f:
				for line in f:
					og = re.search(r"\w*:\s(\w*)", line)
					if og:
						data.append(og.group(1))

def chunks(l, n):
	for i in range(0, len(l), n):			# The 3rd argument n is the stepping distance that i jumps after each iteration.
		yield l[i:i + n]			# Yield is here used in place of return, since it returns a sequence of lists (rather than terminating after the first list is returned).

chunkdata = list(chunks(data, 11))
totalOG = parseTotal.parse_total()			# Retrieving totals dictionary from parseTotal.

propdata = []
i = 0							# Necessary to include counter for loop since the "groupth" iteration not compatible with both dict and list types.

for group in totalOG:					# Calculating genome similarity
	totals = totalOG[group]				# Total values are accessed.
	propdata.append(group)				# Group name is appended corresponding to the relevant data in chunkdata.
	for element in chunkdata[i]:
		proportion = round(int(element) / int(totals) * 100, 2)		# Returns % similarity of genome for each pairwise comparison.
		propdata.append(proportion)
	i += 1

propchunkdata = list(chunks(propdata, 12))		# Divides propdata into lists of proportional data headed by the relevant group.
print(propchunkdata)

output = open("propdata.txt", "w")
outputWrite = output.write(str(propchunkdata))
output.close()
