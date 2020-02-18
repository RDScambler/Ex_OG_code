
def og_list():
	""" This list stores all OG filenames associated with ventral groove -bearing cells """
	og_list = []
	with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/ventral_groove.txt") as f:
		for line in f:
			if line.startswith("OG"):
				og = line.rstrip("\.fal\n\r")
				og_list.append(og)

	return og_list
