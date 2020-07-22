				# This script finds all the OGs of each group, regardless of exclusivity.
				# Outputs are stored in total_genome directory.
import glob
import group
import re

codes = group.alt_codes_18()
group_names = group.alt_groups_18() 		# alt_groups_18() has eukaryote groups SAR and Haptista, as well as 'Other', split into their respective subgroups.

for name in group_names:
	to_parse = glob.glob("*.fal")
	filename = "%s_allOGs.txt" % name
	genome = open(filename, "w")
	i = 0
	for file in to_parse:
		groups_present = []
		with open(file) as f:
			for line in f:
				if line.startswith(">"):
					fields = re.split("_", line)
					species_code = fields[0][1:]
					for code in codes:
						group = codes[species_code]
						if group not in groups_present:
							groups_present.append(group)
		if name in groups_present:							# Functions in the same way as findgroup, only without the exclusive set matching.
			genomeWrite = genome.write(f'{file}\n')
			i += 1
	genomeWrite = genome.write(f'Total gene families in group: {i}')
	genome.close()
