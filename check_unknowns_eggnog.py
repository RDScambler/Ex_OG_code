			# This script scans through all seqs belonging to query taxa that have found no hits in eggnog and compares them to the interpro analyses.
			# The aim is to identify possible functions of otherwise unknown seqs, though annotations may be sparse...

import re
import glob

# Customise taxa as needed.
taxa = "Ancyromonadida_Collodictyonids"
file = (taxa + "_ean_70.0percent.txt")
og_list = []

# Appends to og_list all those OGs with no eggNOG hits.
# These are present in the output file, but have no annotation (thus line length is < 50).
with open(file) as f:
	for line in f:
		if len(line) < 50:
			spline = re.split("\t", line.strip())
			target_og = spline[0]
			if target_og not in og_list:
				og_list.append(target_og)


# interpro_files will work so long as the target taxa alone have .gff3 files in this directory.
# Currently interpro and PANTHER analyses are in separate output files.
interpro_files = glob.glob("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/interpro/interproscan-5.44-79.0/outputs/*.gff3")
output = open(taxa + "_eggnog_nonhits.txt", "w")

# All annotation data relevant to each OG is now parsed out to a new output file.
# Both regular interpro and PANTHER analyses are parsed into this file.
# For this reason the original separate outputs should be used to obtain match_ids for align_matches.py
for og in og_list:
	for file in interpro_files:
		with open(file) as f:
			for line in f:
				res = re.search(og, line)
				if res:
					outputWrite = output.write(line)


# The script will not create the finished file for re-analysis - this is done with grep.
