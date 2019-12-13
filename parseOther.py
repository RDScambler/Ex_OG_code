import re		# *** parseOther.py counts all occurences of each member of 'Other' in Discoba_SplitOther.txt and stores frequencies in a dictionary. ***
import group

codes = group.codes()
othersp = []
frequency = []

for group in codes:					# Creates list of species belonging to 'Other'.
	if codes[group] == "Other":
		othersp.append(group)

for sp in othersp:
	i = 0
	with open("Discoba_SplitOther.txt") as f:
		for line in f:
			res = re.search(sp, line)	# Searches for presence of each species (sp) in output file.
			if res:
				i += 1			# Counts frequency of sp.
	frequency.append(i)				# Appends frequency into a list corresponding to members of othersp.

otherdic = dict(zip(othersp, frequency))		# Zips othersp and frequency lists into a dictionary.
print(otherdic)
