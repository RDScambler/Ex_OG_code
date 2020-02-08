						# *** Template for parsing seqs from .fals into input for eggnog. (Multiple input files do not seem to be possible). ***
output = open("eggnog_toannotate.fal", "w")

with open("ventral_groove.txt") as f:						# Can be adjusted depending on target taxa.
	for line in f:
		if line.startswith("OG"):
			file = line.rstrip("\n\r")				# .rstrip is handy for selectively removing elements of a string.
			with open(file) as f:
				for line in f:
					outputWrite = output.write(line)	# Writes out every sp code and corresponding seq ready for eggnog analysis.
				newline = output.write("\n")			# Separates seqs from different files.
output.close()
