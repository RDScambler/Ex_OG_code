			# This script is configured to output totals data to an Excel file.
			# Could be merged into table_pairwise.py (when I have time!) as I have done with table_pairwise_prop.py.

from openpyxl import Workbook
import re
import group
import glob

# correct_order and group_names can be switched as needed.
# Also remember to configure n in chunks(l, n) to correspond to number of groups in group_names.
# However, correct_order_includingown_18 is for OVERALL total, including the group's own data.
output = open("vector_ordered_propdata_15.txt", "w")
correct_order_12 = ["SAR", "Haptista", "Archaeplastida", "Ancyromonadida", "Telonemids", "Obazoa", "Discoba", "Collodictyonids", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]
correct_order_15 = ["Telonemids", "Haptista", "SAR", "Atwista", "Archaeplastida", "Ancyromonadida", "Obazoa", "Discoba", "Collodictyonids", "Cryptista", "Amoebozoa", "Metamonads", "Hemimastigophora", "Apusomonada", "Malawimonadidae"]

correct_order_includingown_18 = ["Alveolata", "Stramenopiles", "Archaeplastida", "Obazoa", "Telonemids", "Centrohelids", "Ancyromonadida", "Discoba", "Rhizaria", "Cryptista", "Atwista", "Haptophyta", "Collodictyonids", "Amoebozoa", "Metamonads", "Hemimastigophora", "Apusomonada", "Malawimonadidae"]

alt_groups = sorted(group.alt_groups_18())
group_names = alt_groups
data = []

# correct_order_includingown_18 is used here instead of group_names (as in other scripts)
# name is appended to start of each group's data - convenient for outputting in Excel.
for name in correct_order_includingown_18:
	data.append(name)
	to_parse = glob.glob("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/*.txt")
	for file in to_parse:
		filename = re.search(r"([A-Z]\w*)_([A-Z]\w*)_output.txt$", file)
		if filename:
			if filename.group(1) not in group_names:		# Skips 'non-target' files in new_outputs.
				pass
			elif filename.group(2) not in group_names:		# Does the same as above (Since name order in filename can vary).
				pass
			elif filename.group(1) == name:
				shared_og = group.parse_OG(file)
				data.append(shared_og)
			elif filename.group(2) == name:
				shared_og = group.parse_OG(file)
				data.append(shared_og)

def chunks(l, n):
	for i in range(0, len(l), n):			# The 3rd argument n is the stepping distance that i jumps after each iteration.
		yield l[i:i + n]			# Yield is here used in place of return, since it returns a sequence of lists (rather than terminating after the first list is returned).


#Extra element here is for group name in each chunk.
chunkdata = list(chunks(data, 19))			# n MUST be configured depending on number in group_names.

#Creates workbook to output data to Excel.
wb = Workbook()
ws = wb.active

ws.append(group_names)

for row in chunkdata:
	ws.append(row)

wb.save("Pairwise_18.xlsx")
