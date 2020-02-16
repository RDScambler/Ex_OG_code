			# table4.py is modified from the earlier table files.
			# Its purpose is to order and format the pairwise OG data so it enters R in the correct manner.
			# This is the alternative to ordering and formatting in R, which I cannot do at this point.
			# This script will serve my needs until I am more competent in R.
			# minusown list is ordered differently due to differences in total OGs when own groups are excluded.
import re
import group
import glob

group_names = group.groups()
group_names.sort()
data = []
output = open("ordered_vector_data_minusown.txt", "w")

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
correct_order_minusown = ["SAR", "Other", "Haptista", "Discoba", "Archaeplastida", "Obazoa", "Ancyromonadida", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]

for eugroup in correct_order_minusown:									# Choose list as appropriate.
	i = 0
	for pos, name in enumerate(group_names):
		group_data = data[i:i + len(group_names)]						# Captures the data corresponding to the group.
		i += len(group_names)									# i ensures the data index range goes up by 11.
		group_data = [int(number) for number in group_data]					# Converts to a list of ints.
		if name == eugroup:
			for index, x in enumerate(group_data):						# Loop comparing indices of group_names and group_data.
				if index == pos:							# Sets own group values to 0.
					group_data[index] = 0
					translation_table = dict.fromkeys(map(ord, "\w+[',]"), None) 	# This is what I use to strip lists of their punctuation.
					fdata = str(group_data).translate(translation_table)
					outputWrite = output.write(f"{fdata} ")

output.close()
