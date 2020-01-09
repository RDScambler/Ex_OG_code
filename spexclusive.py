import re		# *** spexclusive finds the number of exclusive OGs shared by particular members of 'Other' and Discoba/Ancyromonadida. ***

outlist = ['AtwisOrt', 'DrotaCRt', 'RramoCRt', 'TtrahApg', 'AmaspApt', 'HkukwHmt', 'SmultHmt']					# Testing Telonemids
outlist2 = ['DrotaCRt', 'RramoCRt', 'TtrahApg', 'AmaspApt', 'HkukwHmt', 'SmultHmt', 'TsubtTlt', 'TspP2Tlt', 'TspP1Tlt']		# Testing Atwista
outlist3 = ['AtwisOrt', 'TtrahApg', 'AmaspApt', 'HkukwHmt', 'SmultHmt', 'TsubtTlt', 'TspP2Tlt', 'TspP1Tlt']			# Testing collodictyonids

outlistsA = [outlist, outlist2]

# If none of the outlist group are present in a given line, then it must contain exclusively Telonemid species
# (and at least one representative from 'Discoba'), since these are the remaining 3 member species of 'Other'.
# Each line has at minimum one member of each of the two eukaryote groups. Therefore these OGs are exclusive between the Telonemids and Discoba.
# Same applies for outlist2 and 3 but for Atwista and the collodictyonids, respectively.

output = open("sp_Other_Discoba_exclusives.txt", "w")
targetspp = ["Telonemids", "Ancoracysta twista"]
freq = []

for list in outlistsA:								# Here searching for exclusivity of Telonemids and Atwista in Discoba output file.
	with open("sp_Other_Discoba.txt") as f:
		i = 0
		for line in f:
			linelist = re.split("\W+", line)
			if not set(list).intersection(linelist):		# set.intersection checks if elements are common to both sets.
				i += 1						# Absence of common elements means 'ingroup' of interest is exclusive.
				outputwrite = output.write(f"{linelist}\n")
		freq.append(i)

targetdic = dict(zip(targetspp, freq))
print(targetdic)
outputwrite = output.write(str(targetdic))
output.close()

output2 = open("sp_Other_Ancyromonadida_exclusives.txt", "w")
freq = []
outlistsB = [outlist, outlist3]
targetspp = ["Telonemids", "collodictyonids"]

for list in outlistsB:								# Here searching for exclusivity of Telonemids and collodictyonids in Ancyromonadida output file.
	with open("sp_Other_Ancyromonadida.txt") as f:
		i = 0
		for line in f:
			linelist = re.split("\W+", line)
			if not set(list).intersection(linelist):
				i += 1
				outputwrite = output2.write(f"{linelist}\n")
		freq.append(i)

targetdic2 = dict(zip(targetspp, freq))
print(targetdic2)
outputwrite = output2.write(str(targetdic2))
output2.close()
