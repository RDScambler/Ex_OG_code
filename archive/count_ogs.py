			# Script to count the number of different OG occurences in a file, using regex.
import re
import sys

# Choose file to count OGs of.
file = sys.argv[1]
og_list = []

with open(file) as f:
	for line in f:
		res = re.search(r"(OG\d+)", line.strip())
		if res:
			og = res.group(1)
			if og not in og_list:
				og_list.append(og)

print(og_list)
print(len(og_list))

# Optional: add OGs into a file of your choosing.
output = open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/fa_notes/A_C_fa_summary.md", "a")

for og in og_list:
	outputWrite = output.write(f"{og}\n")
