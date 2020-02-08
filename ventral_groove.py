import glob			# *** Just a small script to parse all the OG output files for all combos of eukaryote groups that have members with ventral groove characters. ***

output = open("ventral_groove.txt", "w")
to_parse = glob.glob("*.txt")
i = 0

for file in to_parse:
	with open(file) as f:
		filename = file.split(".")
		outputWrite = output.write(f"{str(filename[0])}\n")
		for line in f:
			if "Shared" in line:
				pass
			else:
				outputWrite = output.write(line)
				i += 1

total = "Total: "
outputWrite = output.write(f"{total}{i}")
output.close()

