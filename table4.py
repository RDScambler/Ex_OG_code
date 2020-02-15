			# table4.py is modified from the earlier table files.
			# Its purpose is to order and format the pairwise OG data so it enters R in the correct manner.
			# This is the alternative to ordering and formatting in R, which I cannot do at this point.
			# This script will serve my needs until I am more competent in R..
import re
import group
import glob

group_names = group.groups()
group_names.sort()
data = []
output = open("ordered_vector_data.txt", "w")

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

# This list can be modified as needed.
# At this time I have arranged the groups in order of total OGs shared.
# This will result in a more sensible-looking stacked barplot.
correct_order = ["SAR", "Other", "Archaeplastida", "Haptista", "Obazoa", "Discoba", "Ancyromonadida", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]

for eugroup in correct_order:
	i = 0
	for name in group_names:
		group_data = str(data[i:i + len(group_names)])					# Captures the data corresponding to the group.
		i += len(group_names)								# i ensures the data index range goes up by 11.
		if name == eugroup:
			translation_table = dict.fromkeys(map(ord, "\w+[',]"), None) 		# This is what I use to strip lists of their punctuation.
			fdata = group_data.translate(translation_table)
			outputWrite = output.write(f"{fdata} ")

output.close()
