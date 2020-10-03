						# This script takes the output file from parse_file_eg.py.
						# Sequences are parsed from .fals in OG_arb-fal into eggnog_toannotate.fal.

output = open("eggnog_toannotate.fal", "w")

with open() as f:										# Adjust depending on target taxa.
	for line in f:
		if line.startswith("OG"):
			file = line.rstrip("\n\r")						# .rstrip is handy for selectively removing elements of a string.
			with open(file) as f:
				for line in f:
					if line.startswith(">"):
						line = line.rstrip("\n\r") + "_" + file + "\n"	# Formatting to append OG filename to label for unambiguous ID purposes.
						outputWrite = output.write(f"{line}")		# Writes out every sp code and corresponding seq ready for eggnog analysis.
					else:
						outputWrite = output.write(line)
				newline = output.write("\n")					# Separates seqs in different files.
output.close()
