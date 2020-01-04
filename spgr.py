		# Unification of sp and gr modules.
		# The sp module contains sp_find() and sp_count(). Used to find and count species within eukaryote groups.
		# gr functions are similar but modified to return all the groups sharing the OGs of a particular group (i.e similarity NOT exclusivity!).
import re
import group
import glob

def sp_find(eugroup, file):
	"""
	sp_find takes eukaryote group(s) as an argument and searches dataset for matches.
	The file argument is a filename of the user's choosing.
	Like find_group, but prints all its member species alongside filename in the output file.
	sp_count can then be used to count frequencies.
	"""
	setQuery = set(eugroup)
	to_parse = glob.glob("*.fal")
	genome = open(file, "w")
	k = 0
	code_map = group.codes()                        # Defines the code_map imported from group.
	for falfile in to_parse:
		groups_present = []
		sp_present = []
		with open(falfile) as f:
			for line in f:
				if line.startswith('>'):
					fields = re.split('_', line)                            # Separates sp. code
					species_code = fields[0][1:]                            # Removes '>'
					for i in code_map:                                      # Linking sp. code to group
						gr = code_map[species_code]
						if gr not in groups_present:               	# Adding to group array if new group
							groups_present.append(gr)
						if gr in eugroup:
							if species_code not in sp_present:      # Appends species to sp_present if they are members of group.
								sp_present.append(species_code)
		set_present = set(groups_present)
		if setQuery == set_present:
			genomewrite = genome.write(f'{falfile}\t{sp_present}\n')           	# Adds file plus species present to output if it matches query
			k += 1                                                          	# Counter for total number of OG matches.

	genomewrite = genome.write(f'Shared gene families: {k}')
	genome.close()


def gr_find(eugroup, file):
	"""
	gr_find takes eukaryote group(s) as an argument and searches dataset for matches.
	Prints all groups that share each gene of the query group's genome in the output file.
	gr_count can then be used to count frequencies.
	"""
	to_parse = glob.glob("*.fal")
	genome = open(file, "w")
	k = 0
	code_map = group.codes()                        # Defines the code_map imported from group.
	for falfile in to_parse:
		groups_present = []
		with open(falfile) as f:
			for line in f:
				if line.startswith('>'):
					fields = re.split('_', line)                            # Separates sp. code
					species_code = fields[0][1:]                            # Removes '>'
					for i in code_map:                                      # Linking sp. code to group
						gr = code_map[species_code]
						if gr not in groups_present:               	# Adding to group array if new group
							groups_present.append(gr)

		if eugroup in groups_present:
			genomewrite = genome.write(f'{falfile}\t{groups_present}\n')           	# Adds file plus groups present in that file.
			k += 1                                                          	# Counter for total number of OG matches.

	genomewrite = genome.write(f'Shared gene families: {k}')
	genome.close()


def sp_count(eugroup, file):
	"""sp_count takes a eukaryote group as an argument and counts all occurences of each sp of the group in selected file and stores frequencies in a dictionary."""
	codes = group.codes()
	splist = []
	frequency = []

	for groupname in codes:					# Creates list of species belonging to the group.
		gr = codes[groupname]
		if gr == eugroup:
			splist.append(groupname)

	for sp in splist:
		i = 0
		with open(file) as f:
			for line in f:
				res = re.search(sp, line)	# Searches for presence of each species (sp) in output file.
				if res:
					i += 1			# Counts frequency of sp.
		frequency.append(i)				# Appends frequency into a list corresponding to members of splist.

	spdic = dict(zip(splist, frequency))			# Zips splist and frequency lists into a dictionary.
	return spdic


def gr_count(file):
	"""gr_count takes an output file (i.e. one from gr_find) as an argument, counts all occurences of each eukaryote group in selected file and stores frequencies in a dictionary."""
	codes = group.codes()
	grlist = []
	frequency = []

	for groupname in codes:					# Creates group list.
		group1 = codes[groupname]
		if group1 not in grlist:
			grlist.append(group1)

	for gr in grlist:
		i = 0
		with open(file) as f:
			for line in f:
				res = re.search(gr, line)	# Searches for presence of each group (gr) in output file.
				if res:
					i += 1			# Counts frequency of gr.
		frequency.append(i)				# Appends frequency into a list corresponding to members of grlist.

	grdic = dict(zip(grlist, frequency))			# Zips grlist and frequency lists into a dictionary.
	return grdic
