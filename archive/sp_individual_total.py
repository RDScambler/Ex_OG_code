import group
import glob
import re

codes = group.alt_codes_18()
sp_list = []

for sp in codes:
	sp_list.append(sp)

to_parse = glob.glob("*.fal")

for sp in sp_list:
	filename = "%s_total.txt" % sp
	output = open(filename, "w")
	k = 0
	for file in to_parse:
		species_present = []
		with open(file) as f:
			for line in f:
				if line.startswith(">"):
					fields = re.split("_", line)
					species = fields[0][1:]
					if sp == species:
						if species not in species_present:
							species_present.append(species)
							outputWrite = output.write(f"{file}\n")
							k += 1
	outputWrite = output.write(f"{sp} total OGs: {k}")
	output.close()
