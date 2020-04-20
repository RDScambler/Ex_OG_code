			# table_pairwise is modified from table4.py. It is designed to parse the 'Other subgroups' pairwise data.
			# It differs by skipping over 'Other' files in new_outputs, and adding the correct_order_minusown_alt list.
			# Its purpose is to order and format the pairwise OG data so it enters R in the correct manner.
			# This is the alternative to ordering and formatting in R, which I cannot do at this point.
			# This script will serve my needs until I am more competent in R.
			# minusown list is ordered differently due to differences in total OGs when own groups are excluded.
import re
import group
import glob

# group_names can be configured depending on the groups in need of processing.
# split_groups_18 now includes split SAR and Haptista.
# Should correctly work through output files in new_outputs assuming all target groups are contained within group_names.
group_names = ["Amoebozoa", "Ancyromonadida", "Archaeplastida", "Collodictyonids", "Cryptista", "Discoba", "Haptista", "Malawimonadidae", "Metamonads", "Obazoa", "SAR", "Telonemids"]
split_groups_18 = sorted(group.split_groups_18())
group_names = split_groups_18
data = []
output = open("ordered_vector_data_minusown_18.txt", "w")

for name in group_names:
	to_parse = glob.glob("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/*.txt")
	for file in to_parse:
		filename = re.search(r"([A-Z]\w+)_([A-Z]\w+)_output.txt$", file)
		if filename:
			if filename.group(1) not in group_names:		# Skips files in new_outputs (if certain groups are being excluded).
				pass
			elif filename.group(2) not in group_names:		# Does the same as above (Since name order in filename can vary).
				pass
			elif filename.group(1) == name:
				shared_og = group.parse_OG(file)
				data.append(shared_og)
			elif filename.group(2) == name:
				shared_og = group.parse_OG(file)
				data.append(shared_og)

# This list can be modified as needed.
# At this time I have arranged the groups in order of total OGs shared.
# This will result in a more sensible-looking stacked barplot.
# The 12 and 15 are split 'Other' subgroups, 18 also splits SAR and Haptista.
correct_order = ["SAR", "Other", "Archaeplastida", "Haptista", "Obazoa", "Discoba", "Ancyromonadida", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]
correct_order_minusown = ["SAR", "Other", "Haptista", "Discoba", "Archaeplastida", "Obazoa", "Ancyromonadida", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]
correct_order_minusown_12 = ["SAR", "Haptista", "Archaeplastida", "Obazoa", "Telonemids", "Ancyromonadida", "Discoba", "Cryptista", "Collodictyonids", "Amoebozoa", "Metamonads", "Malawimonadidae"]
correct_order_minusown_15 = ["SAR", "Haptista", "Telonemids", "Archaeplastida", "Obazoa", "Ancyromonadida", "Discoba", "Atwista", "Cryptista", "Collodictyonids", "Amoebozoa", "Metamonads", "Hemimastigophora", "Apusomonada", "Malawimonadidae"]
correct_order_minusown_18 = ["Alveolata", "Telonemids", "Stramenopiles", "Archaeplastida", "Obazoa", "Centrohelids", "Ancyromonadida", "Discoba", "Atwista", "Haptophyta", "Cryptista", "Rhizaria", "Collodictyonids", "Amoebozoa", "Metamonads", "Hemimastigophora", "Apusomonada", "Malawimonadidae"]

for eugroup in correct_order_minusown_18:								# Choose list as appropriate.
	i = 0
	for pos, name in enumerate(group_names):
		group_data = data[i:i + len(group_names)]						# Captures the data corresponding to the group.
		i += len(group_names)									# i ensures the data index range goes up by length of list..
		group_data = [int(number) for number in group_data]					# Converts to a list of ints.
		if name == eugroup:
			for index, x in enumerate(group_data):						# Loop comparing indices of group_names and group_data.
				if index == pos:							# Sets own group values to 0.
					group_data[index] = 0
					translation_table = dict.fromkeys(map(ord, "\w+[',]"), None) 	# This is what I use to strip lists of their punctuation.
					fdata = str(group_data).translate(translation_table)
					outputWrite = output.write(f"{fdata} ")

output.close()
