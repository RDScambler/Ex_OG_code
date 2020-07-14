				# group module. Contains all necessary functions involved in the OG pipeline.
				# Incorporates code from old parse_OG.py and parse_total.py files (integrated for clarity/convenience).
				# NOTE: at some point can incorporate codes() functions into 1 function with file as argument. Same for group_name lists.
				# However, this would mean many scripts would need to be altered, so maybe not...
import re
import glob

def codes():
	"""codes returns a dictionary containing sp.codes as keys and eukaryote groups as values. This can be used to search through genomic data for presence/absence of particular groups."""
	code_map = {}
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/Eukaryote_codes.txt") as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
	return code_map

def alt_codes():
	"""alt_codes returns a dictionary with the 'Other' eukaryote group divided into subgroups according to their phylogenetic relationships."""
	code_map = {}
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/Eukaryote_codes_alt.txt") as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
	return code_map

def alt_codes_18():
	"""alt_codes_18 returns a dictionary with 'SAR' and Haptista divided into their respective subgroups."""
	code_map = {}
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/Eukaryote_codes_alt_18.txt") as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
	return code_map

def long_name_codes(code_map):
	"""long_name_codes is an alternative to the other code maps, returning full sp. names instead of just abbreviations.
	To avoid remaking different code maps for different group splits, this function takes one of the original code maps as an argument. """
	long_name_code_map = {}

	for sp_code in code_map:
		group = code_map[sp_code]
		# Note: this file is currently used as a source for the names, but in principle any file containing all the long names could be used.
		# The creation of a source file (i.e. a new Eukaryotes_codes.txt) is avoided since this would reduce flexibility when switching between group splits.
		with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/iqtree/Ancyromonads_Collodictyonids/Ancyromonads_Collodictyonids.constr") as f:
			for line in f:
				res = re.search(sp_code + r"(_\w+-\w+)", line.strip())
				if res:
					long_name = res.group(1)
					full_name = sp_code + long_name
					long_name_code_map[full_name] = group

	return long_name_code_map

def groups():
	"""groups uses the dictionary defined in codes() to create an array containing all eukaryote groups in dataset."""
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

def split_groups_18():
	"""split_groups_18 returns a group list with 'Other', SAR and Haptista all divided into subgroups."""
	group_names = []
	spcode = alt_codes_18()
	for group in spcode.values():
		if group not in group_names:
			group_names.append(group)
	return group_names

def parse_OG(file):
	""" parse_OG is designed to parse out the 'Shared gene families: ' data from find_group() output files."""
	with open(file) as f:
		for line in f:
			og = re.search(r"\w*:\s(\w*)", line)			# I.e. "Shared gene families: NNNN"
			if og:
				return og.group(1)

def count_ogs(file):
	"""count_ogs searches through any document and appends to a list all the different OG strings.
	This regex is not specified with any preceding "_" or trailing ".fal" due to the variety of contexts OGs may occur in."""
	og_list = []
	with open(file) as f:
		for line in f:
			res = re.search(r"(OG\d{7})", line.strip())
			if res:
				og = res.group(1)
				if og not in og_list:
					og_list.append(og)
	return og_list

def parse_total():
	"""parse_total returns a dictionary with the total number of OGs that each group has. Expanded from the original to include the 'Other' subgroups."""
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/summary_data/group_total.txt") as f:
		group = []
		total =[]
		for line in f:
			spline = re.split("\t", line.strip())
			group.append(spline[0].strip())
			total.append(spline[1])

		totaldic = dict(zip(group, total))
		return totaldic

def sp_total_dic():
	"""sp_total_dic iterates over every file in sp_individual_total/, and stores the total number of OGs that each sp. has in a dictionary. """
	codes = group.alt_codes_18()
	to_parse = glob.glob("sp_individual_total/*.txt")
	sp_list = []
	sp_total_dic = {}
	for sp in codes:
		sp_list.append(sp)
	for sp in sp_list:
		for file in to_parse:
			split_path = re.split(r"/", file)
			split_file = re.split(r"_", split_path[1])
			if split_file[0] == sp:
				total = group.parse_OG(file)
				sp_total_dic[sp] = total

	return sp_total_dic

def find_group(set_query, code_map):
	"""find_group takes a set as an argument, potentially from a user's input, to be compared with the set of groups_present in each .fal file in directory.
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
	genomewrite = genome.write(f'{set_query}\n')
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
