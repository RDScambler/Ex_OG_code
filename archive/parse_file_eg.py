			# This script parses all the OG output filenames relevant to the biological question.
			# to_parse assumes directory is comprised entirely of output files that need to be parsed.
			# output variable filename must of course be edited as necessary.
import glob

output = open(, "w")
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

