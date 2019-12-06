import re				# *** group module. codes(), groups() and find_group() functions are defined here. ***
import glob

def codes():
	"""codes() returns a dictionary containing sp.codes as keys and eukaryote groups as values. This can be used to search through genomic data for presence/absence of particular groups."""
	code_map = {}
	with open('Eukaryote_codes.txt') as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
	return code_map

def groups():
	"""groups() uses the dictionary defined in codes() to create an array containing all eukaryote groups in dataset."""
	group_names = []
	spcode = codes()
	for group in spcode.values():
		if group not in group_names:
			group_names.append(group)
	return group_names

def find_group(setQuery):
	"""find_group() takes a set as an argument, potentially from a user's input, to be compared with the set of groups_present in each .fal file in directory. Matching files are written to an output file with the set elements (i.e. group names) as the file title."""
	to_parse = glob.glob("*.fal")
	filename = "_".join(setQuery)                   # Joins set into a sensible filename.
	genome = open(filename + ".txt", "w")
	k = 0
	code_map = codes()                        # Defines the code_map imported from group.
	for file in to_parse:
		groups_present = []
		with open(file) as f:
			for line in f:
				if line.startswith('>'):
					fields = re.split('_', line)                    # Separates sp. code
					species_code = fields[0][1:]                    # Removes '>'
					for i in code_map:                              # Linking sp. code to group
						eugroup = code_map[species_code]
						if eugroup not in groups_present:       # Adding to group array if new group
							groups_present.append(eugroup)
		set_present = set(groups_present)
		if setQuery == set_present:
			genomewrite = genome.write(f'{file}\n')                         # Adds file to output if it matches query
			k += 1                                                          # Counter for total number of OG matches.
	genomewrite = genome.write(f'Shared gene families: {k}')
	genome.close()
