
				# group module. codes(), groups(), split_other_groups(), parse_OG(), parse_total() and find_group() functions are defined here.
				# Incorporates code from old parse_OG.py and parse_total.py files (integrated for clarity/convenience).
import re
import glob

def codes():
	"""codes() returns a dictionary containing sp.codes as keys and eukaryote groups as values. This can be used to search through genomic data for presence/absence of particular groups."""
	code_map = {}
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/Eukaryote_codes.txt") as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
	return code_map

def alt_codes():
	"""alt_codes() returns a dictionary with the 'Other' eukaryote group divided into subgroups according to their phylogenetic relationships."""
	code_map = {}
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/Eukaryote_codes_alt.txt") as f:
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

def split_other_groups():
	"""split_other_groups returns a similar list to the original groups(), however 'Other' is divided into its various subgroups."""
	group_names = []
	spcode = alt_codes()
	for group in spcode.values():
		if group not in group_names:
			group_names.append(group)
	return group_names

def parse_OG(file):
	""" parse_OG() is designed to parse out the 'Shared gene families: ' data from find_group() output files."""
	with open(file) as f:
		for line in f:
			og = re.search(r"\w*:\s(\w*)", line)			# I.e. "Shared gene families: NNNN"
			if og:
				return og.group(1)

def parse_total():
	"""parse_total() returns a dictionary with the total number of OGs that each group has. Expanded from the original to include the 'Other' subgroups."""
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/summary_data/group_total.txt") as f:
		group = []
		total =[]
		for line in f:
			spline = re.split("\t", line.strip())
			group.append(spline[0].strip())
			total.append(spline[1])

		totaldic = dict(zip(group, total))
		return totaldic

def find_group(set_query, code_map):
	"""find_group() takes a set as an argument, potentially from a user's input, to be compared with the set of groups_present in each .fal file in directory.
	Matching files are written to an output file with the set elements (i.e. group names) as the file title.
	The code_map ought to be chosen from either codes() or alt_codes(), depending on whether or not the 'Other' subgroups are being queried.
	It is important here that the data type of set_query is correct (i.e list if a single element, set if multiple elements).
	Otherwise, set_present and set_query may not match. The initial if/else loop ensures the data type is correct (using x)."""
	to_parse = glob.glob("*.fal")
	if isinstance(set_query, list):
		filename = "_".join(set_query)						# Joins set into a sensible filename.
		x = 0									# x necessary as a conditional in place of isinstance(set_query, list) - see loop further down.
	else:
		filename = set_query
		set_query = [set_query]							# [] necessary to match the str set_query to groups_present (which is a single element list).
		x = 1
	genome = open(filename + "_output.txt", "w")
	k = 0
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
		if x == 0:								# Turns multiple element lists into sets.
			set_present = set(groups_present)
			set_query = set(set_query)					# if isinstance(set_query, list) not used since this would convert it to a set after first iteration.
		else:									# Single elements (i.e own group comparisons) must remain as they are.
			set_present = groups_present
		if set_query == set_present:
			genomewrite = genome.write(f'{file}\n')				# Adds file to output if it matches query
			k += 1                                                          # Counter for total number of OG matches.
	genomewrite = genome.write(f'Shared gene families: {k}')
	genome.close()
