
def full_og_list(file):
	""" This list stores all OG filenames associated with a particular biological question.
	    Can be useful in post-eggnog analysis. Input file should contain relevant OG filenames only.
	    (extra text will interfere with function). """

	full_og_list = []
	with open(file) as f:
		for line in f:
			if line.startswith("OG"):
				og = line.rstrip("\.fal\n\r")
				full_og_list.append(og)

	return full_og_list
