# Can make a db using makeblastdb in command line:

import glob

to_parse = glob.glob("OG*.fal")
output = open("97_proteome.fal", "w")

for file in to_parse:
	with open(file) as f:
		for line in f:
			if line.startswith(">"):
				line = line.rstrip("\n\r") + "_" + file + "\n"
				outputWrite = output.write(line)
			else:
				outputWrite = output.write(line)
output.close()
