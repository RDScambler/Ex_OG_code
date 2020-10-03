import glob					# *** Finds total OGs for subgroups of 'Other'. ***
import re

telonemids = ['TspP1Tlt', 'TspP2Tlt', 'TsubtTlt']
collodictyonids = ['DrotaCRt', 'RramoCRt',]
apusomonada = ['TtrahApg', 'AmaspApt']
hemimastigophora = ['HkukwHmt', 'SmultHmt']
atwista = ['AtwisOrt']

groups = [telonemids, collodictyonids, apusomonada, hemimastigophora, atwista]


for group in groups:
	to_parse = glob.glob("*.fal")
	filename = "%s_allOGs.txt" % group							# Minor bug - literal lists are printed in output filename.
	genome = open(filename, "w")
	i = 0
	for file in to_parse:
		species_present = []
		with open(file) as f:
			for line in f:
				if line.startswith(">"):
					fields = re.split("_", line)
					species_code = fields[0][1:]
					if species_code not in species_present:
							species_present.append(species_code)

		if set(group).intersection(species_present):					# Checks for commonalities between spp. in file and the group being queried.
			genomeWrite = genome.write(f'{file}\n')
			i += 1
	genomeWrite = genome.write(f'Total gene families in group: {i}')
	genome.close()
