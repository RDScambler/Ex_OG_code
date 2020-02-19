
			# table2.py extracts the same data as table.py, but converts the pairwise OGs to % total for each group.
			# Now modified for ease of use in R. Proportional data is correctly ordered, and within-group data set to 0.
			# Final loop is taken from table4.py.
import re
import group
import glob
import parseTotal

# correct_order and group_names can be switched as needed.
# correct_order is correct for proportion of total genome shared.
output = open("vector_ordered_propdata.txt", "w")
correct_order = ["Other", "Discoba", "Haptista", "SAR", "Ancyromonadida", "Archaeplastida", "Obazoa", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]
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

for group in group_names:				# Calculating genome similarity
	totals = totalOG[group]				# Total values are accessed.
							# propdata.append(group) can be added here if desired (group name is appended corresponding to the relevant data in chunkdata).
	for element in chunkdata[i]:
		proportion = round(int(element) / int(totals) * 100, 2)		# Returns % similarity of genome for each pairwise comparison.
		propdata.append(proportion)
	i += 1

for eugroup in correct_order:										# Choose list as appropriate.
	j = 0
	for pos, name in enumerate(group_names):
		group_data = propdata[j:j + len(group_names)]						# Captures the data corresponding to the group.
		j += len(group_names)									# j ensures the data index range goes up by 11.
		group_data = [float(number) for number in group_data]					# Converts to a list of floats (for proportion)..
		if name == eugroup:
			for index, x in enumerate(group_data):						# Loop comparing indices of group_names and group_data.
				if index == pos:							# Sets own group values to 0.
					group_data[index] = 0
					translation_table = dict.fromkeys(map(ord, "\w+[',]"), None) 	# This is what I use to strip lists of their punctuation.
					fdata = str(group_data).translate(translation_table)
					outputWrite = output.write(f"{fdata} ")
			x = sum(group_data)
			print(x)

output.close()
