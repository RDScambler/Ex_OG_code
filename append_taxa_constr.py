			# This script is used to output sp. codes into a constraint file for topological constraint testing in IQ-TREE.
			# Specify the groups of interest, and select the necessary code map (12, 15, 18).
			# Use long_name_codes for the 42 alignment (otherwise the original sp_codes work for the 116 alignment).

import sys
import re
sys.path.insert(0, "/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/OG_results_pipeline/")
import group

# Choose group(s) to be constrained.
groups_of_interest = ["Telonemids", "SAR"]

# Select code map as necessary.
# long_name_codes can take any of the original code maps as an argument.
# These are converted into the long sp. names as found in the 42 alignment file.
codes = group.alt_codes()
codes = group.long_name_codes(codes)
sp_codes = []

# Extract necessary sp. codes from dict.
# Currently set to 15-way split codes (since SAR is target group).
for group in groups_of_interest:
	for g in codes:
		gr = codes[g]
		if gr == group:
			sp_codes.append(g)

# Configure filename as necessary.
output = open("SAR_Telonemids.constr", "w")
other_taxa = []

# Adds the necessary brackets.
sp_codes[0] = "((" + sp_codes[0]
sp_codes[-1] = sp_codes[-1] + ")"

# Output ingroup sp. names into constr. file.
for sp in sp_codes:
	outputWrite = output.write(f"{sp}{', '}")

# Output outgroup taxa.
with open("116_congruent_genes_phyltered.fas") as f:
	for line in f:
		res = re.search(r"^>(\w*)", line.strip())
		if res:
			a = res.group(1)
			if a not in sp_codes:
				fline = a + ", "
				outputWrite = output.write(fline)

outputWrite = output.write(");")
output.close()
