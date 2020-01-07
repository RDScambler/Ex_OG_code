import spgr		# *** Calculates the proportion of shared genome for each eukaryote group. ***
import group
import parseTotal

groups = group.groups()
output = open("gr_prop_freq_output.txt", "w")
totaldic = parseTotal.parse_total()

for g in groups:
	proplist = []
	filename = "gr_" + g + ".txt"
	res = spgr.gr_count(filename)				# gr_count is carried out on the relevant output file.
	total = totaldic[g]					# Total genome size is accessed for each group
	for name in res:
		og = res[name]					# Number of OGs shared with group g is compared for every group.
		prop = round(int(og) / int(total) * 100, 2)	# Proportion is calculated.
		proplist.append(prop)
	propdic = dict(zip(groups, proplist))			# Proportion dictionary is created.
	print(propdic)
	outputWrite = output.write(f"{g}\t{str(propdic)}\n")

output.close()
