import re			# *** 'Other' is here partitioned into phylogenetically relevant subgroups to find their unique OGs. ***

output = open("sp_Other_exclusivesubgroups.txt", "w")

telonemids = ['TspP1Tlt', 'TspP2Tlt', 'TsubtTlt']					# Relevant subgroups are made into lists.
collodictyonids = ['DrotaCRt', 'RramoCRt',]
apusomonada = ['TtrahApg', 'AmaspApt']
hemimastigophora = ['HkukwHmt', 'SmultHmt']
atwista = ['AtwisOrt']

subgroups = [telonemids, collodictyonids, apusomonada, hemimastigophora, atwista]	# List of lists created for looping over.
freq = []

for subgroup in subgroups:
	i = 0
	with open("sp_Other.txt") as f:							# Original output file of all unique 'Other' OGs.
		for line in f:
			translation_table = dict.fromkeys(map(ord, "[',]"), None)	# translation_table created as method of removing unwanted characters from line (all are mapped to none).
			linef = line.translate(translation_table)			# This then no superfluous characters are present when splitting line into a list.
			res = re.split(r"\s+", linef.strip())				# Perhaps there is a better way of doing this(???)
			if all(elem in subgroup for elem in res[1:]):			# all() determines whether or not all members of the line are contained within the subgroup query.
				i += 1							# res[1:] omits OG filename from the comparison.
				outputWrite = output.write(f"{res}\n")
	freq.append(i)
	outputWrite = output.write("\n")

subgroups = ['Telonemids', 'Collodictyonids', 'Apusomonada', 'Hemimastigophora', 'Ancoracysta twista']

subgroupdic = dict(zip(subgroups, freq))
print(subgroupdic)
outputWrite = output.write(str(subgroupdic))
output.close()
