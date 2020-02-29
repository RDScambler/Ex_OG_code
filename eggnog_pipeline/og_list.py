
def og_list(file):
	""" This list stores all OG filenames associated with a particular biological question.
	    Can be useful in post-eggnog analysis. Input file should be a list of relevant OG filenames. """

	og_list = []
	with open(file) as f:
		for line in f:
			if line.startswith("OG"):
				og = line.rstrip("\.fal\n\r")
				og_list.append(og)

	return og_list
