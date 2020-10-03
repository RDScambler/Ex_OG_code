import re			# *** table.py creates a table from the output files, with each element in each list corresponding to the same eukaryote group (arranged alphabetically).
import group
import glob

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

chunkdata = chunks(data, 11)

output = open("pairwise_groups_tableformat.txt", "w")
row_format = "{:>11}" * (len(group_names) + 1)
headers = row_format.format("", *group_names)
outputWrite = output.write(f"{headers}\n")					# Generates each group name as a header.
for group, row in zip(group_names, chunkdata):					# zip creates a dictionary type linking each list within chunkdata to the relevant group.
	outputWrite = output.write(f"{row_format.format(group, *row)}\n")	# Writes out the data as a table. row_format ensures table contents align with relevant header (although this isn't exactly perfect...).

