			# total.py is the new, integrated file that processes total OG data (formerly carried out by parseOG.py and groupdata.py).
			# The related functions, parse_total() (from parseTotal.py) and parse_OG (from parseOG.py) are now incorporated into the group module.
			# split_other_group() has also been added to group.py to include relevant subgroups from 'Other' in a new list.

import glob
import group
import re

# To be executed in total_genome dir.
# 18 groups list is currently being used.
to_parse = glob.glob("*_allOGs.txt")
output = open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_Data/OG_arb-fal/new_outputs/summary_data/group_total.txt", "w")
original_groups = group.groups()
correct_order_groups_15 = ["SAR", "Haptista", "Archaeplastida", "Obazoa", "Telonemids", "Discoba", "Ancyromonadida", "Cryptista", "Atwista", "Amoebozoa", "Collodictyonids", "Metamonads", "Apusomonada", "Hemimastigophora", "Malawimonadidae"]
correct_order_groups_18 = ["Alveolata", "Stramenopiles", "Archaeplastida", "Obazoa", "Telonemids", "Discoba", "Centrohelids", "Ancyromonadida", "Cryptista", "Rhizaria", "Haptyophyta", "Atwista", "Amoebozoa", "Collodictyonids", "Metamonads", "Apusomonada", "Hemimastigophora", "Malawimonadidae"]

for file in to_parse:
	name = re.split("_", file)
	og = group.parse_OG(file)
	outputWrite = output.write(f"{name[0]}\t{og}\n")

output.close()

# Writes out totals and own OGs to a file as a single vector.
# The data can then be processed in R.
own_OGs_to_parse = glob.glob("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/*.txt")
totals_own_output = open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/summary_data/vector_totals_own_18.txt", "w")

# correct_order_groups must be at top of loop to ensure correct order is maintained.
# list of choice can be configured here.
for eugroup in correct_order_groups_18:
	for file in own_OGs_to_parse:
		res = re.search(r"(\w+)_(\w+)_output.txt$", file)
		if res:
			if res.group(1) == res.group(2):
				if eugroup == res.group(1):
					totaldic = group.parse_total()			# parse_total() contains all totals data (inc. Other AND all its subgroups).
					total = totaldic[eugroup]
					own = group.parse_OG(file)
					outputWrite = totals_own_output.write(f"{total} {own} ")	# Output formatted for R.


