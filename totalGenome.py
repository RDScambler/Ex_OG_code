import glob
import re

code_map = {}
group_names = []

with open('Eukaryote_codes.txt') as f:
    for line in f:
        fields = re.split("\t", line.strip())
        code_map[fields[0]] = fields[1]
        if fields[1] not in group_names:
            group_names.append(fields[1])

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
					for code in code_map:
						group = code_map[species_code]
						if group not in groups_present:
							groups_present.append(group)
		if name in groups_present:							# Functions in the same way as findgroup, only without the exclusive set matching.
			genomeWrite = genome.write(f'{file}\n')
			i += 1
	genomeWrite = genome.write(f'Total gene families in group: {i}')
	genome.close()
