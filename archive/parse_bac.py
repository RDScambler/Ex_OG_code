				# *** This script parses bacterial hits and euk/archaea hits into separate outputs. ***
import re

bac_output = open("ventral_groove_bac.txt", "w")
euk_arc_output = open("ventral_groove_euk_arc.txt", "w")
bac_list = []
euk_arc_list = []

with open("ventral_groove_refined_eg.txt") as f:
	for line in f:
		if len(line) < 2:							# Skips empty lines.
			pass
		else:
			spline = re.split("\s+", line.strip(), maxsplit=6)		# maxsplit=6 keeps the text description as a single string at end of list.
			og = spline[0]
			tax = spline[5]
			if tax == "Bacteria":
				if og not in bac_list:					# Appends bacterial ogs to list.
					bac_list.append(og)
			else:
				if og not in euk_arc_list:				# Appends euk/archaeal ogs to separate list.
					euk_arc_list.append(og)				# Since the eggnog hits from the same og yield hits from multiple domains, there will be overlap in lists.

with open("ventral_groove_refined_eg.txt") as f:					# Had to open second loop - for some reason repeating "for line in f" in same loop has no effect.
	for line in f:
		for og in bac_list:							# Checks every og against every line.
			if og in line:
				bac_outputWrite = bac_output.write(line)
#		if len(line) < 2:							# Writing newline between ogs - currently left out. It corresponds to all blank lines in file
#			bac_outputWrite = bac_output.write("\n")			# (not just those following bacterial ogs).

		for og in euk_arc_list:							# Same process is carried out for non-bacterial hits.
			if og in line:
				euk_arc_outputWrite = euk_arc_output.write(line)

bac_output.close()
euk_arc_output.close()
