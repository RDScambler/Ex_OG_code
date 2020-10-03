			# Script written to sum all the ubiquitous or near-ubiquitous OGs in the dataset.
			# This is summarised in the printed output.

import sys
sys.path.insert (0, "/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/OG_results_pipeline")
import group
import glob

split_system = [15, 18]

for system in split_system:
	sum = 0
	if system == 15:
		to_parse = glob.glob("*_15_output.txt")
	else:
		to_parse = glob.glob("*_18_output.txt")
	for file in to_parse:
		filename = file.split("_")
		if "common" in filename:				# Finds output file containing OGs common to all groups.
			common = int(group.parse_OG(file))
		else:
			total_OGs = int(group.parse_OG(file))		# Finds the relevant output files (15 or 18).
			sum = sum + total_OGs				# sum accrues the total for all output files over the course of the loop.

	total = str(sum + common)
	print("The number of orthogroups common to every eukaryote group (" + str(system) + "-way split) is " + str(common) +
		". An additional " + str(sum) + " are common to every group but one, for a total of " + total + " ubiquitous or near-ubiquitous orthogroups.")
