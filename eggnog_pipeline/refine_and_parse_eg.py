			# Script for improving the readability of eggnog output files.
			# In principle should be applicable to all outputs, providing sp labels are suffixed with "_OGxxxxxxx".
			# Important not to discard raw .emapper.annotations files since GOs, kegg etc. are not transferred.
			# Script also parses out all ogs that have no hits in eggnog to a separate file.
			# Script now also parses bacterial and non-bacterial OGs using a customisable cutoff point.
			# These different processes are incorporated here since they all make use of the same og_list.
			# Summary stats now added, and query name requested for convenience.
import re
import group
import full_og_list

query = input("Enter the name of your query (e.g. Metamonads_Discoba): \n")
output = open(query + "_refined_eg.txt", "w")

codes = group.alt_codes()
og_list = []
preanno_full_list = full_og_list.full_og_list("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/" + query + "_output.txt")
species_list = []
sp_label_regex = "(\w{,8})_\w*[tn|gn]\d+_(\w+\-\w+)_(OG\d+)"					# Splits up the first entry of output file (these are not tab-separated).

with open(query + ".emapper.annotations") as f:							# Filename must be edited as necessary.
	for line in f:
		res = re.search(sp_label_regex, line)
		if res:
			sp_code = res.group(1)
			sp_name = res.group(2)
			if sp_name not in species_list:						# Making this list to conveniently get a list of all ventral-groovers.
				species_list.append(sp_name)					# Worth noting this may exclude some taxa only captured in pairwise analysis.
			og = res.group(3)
			eugroup = codes[sp_code]						# Eukaryote group is derived from the codes dict.
			fnames = eugroup.ljust(20) + sp_name.ljust(30)				# .ljust formats for appearance.
			tabline = re.split("\t", line.strip())
			e = tabline[2].ljust(15)
			ftax_hit = tabline[4].replace(" ", "_").ljust(40)			# Removing whitespace from between tax_hit strings (for ease of future parsing).
			gene_id = tabline[5].ljust(10)
			tax_scope = tabline[17].ljust(20)
			text_description = tabline[-1]
			if og not in og_list:							# Appends ogs to og_list for the purposes of identifying new ogs and inserting \n accordingly.
				og_list.append(og)
				outputWrite = output.write("\n")
			outputWrite = output.write(f"{og}\t{fnames}{e}{ftax_hit}{tax_scope}{gene_id}{text_description}\n")

output.close()

# Here a cutoff point is requested.
# This can be customised as required.
# The proportion defines how many bacterial sequences can make up the eukaryote/archaea output file.
# I.e what level is being considered as homologous rather than a contaminant.

while True:
	cutoff = float(input("What is the bacterial cutoff point for orthogroups (as a proportion of the group's sequences)?\n"))
	if cutoff < 1 and cutoff > 0:
		break
	else:
		print("Enter a proportion for cutoff (between 0 and 1).")

# ean = Eukaryotes, Archaea, no hits.
ean_output = open(query + "_ean_" + str(cutoff * 100) + "percent.txt", "w")
bac_output = open(query + "_bac_" + str(cutoff * 100) + "percent.txt", "w")

euk_arc_list = []
bac_list = []

for og in og_list:
	j = 0
	tax_list = []
	while j < 2:														# While loop is necessary to iterate over the file twice.
		i = 0														# The first loop appends all taxa in og to tax_list.
		with open(query + "_refined_eg.txt") as f:						# The second compares the frequency of Bacterial seqs to the cutoff.
			if j < 1:
				for line in f:
					if og in line:
						spline = re.split(r"\s+", line.strip(), maxsplit=6)
						tax = spline[5]
						tax_list.append(tax)
			else:
				for taxon in tax_list:
					if taxon == "Bacteria":
						i += 1
				if i < cutoff * len(tax_list):									# If below the cutoff, ogs are written to the euk/arc output file.
					for line in f:
						if og in line:
							outputWrite = ean_output.write(line)
							if og not in euk_arc_list:						# For the purposes of collecting summary stats.
								euk_arc_list.append(og)
				else:												# Otherwise they are written to the bacterial output file.
					for line in f:
						if og in line:
							outputWrite = bac_output.write(line)
							if og not in bac_list:
								bac_list.append(og)
		j += 1														# j ensures while loop occurs twice.

bac_output.close()

for og in preanno_full_list:
	if og not in og_list:													# Identifies ogs not analysed by eggnog.
		with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/eggnog-mapper/eggnog_toannotate.fal") as f:		# opens pre-annotation file.
			for line in f:
				if og in line:
					res = re.search(sp_label_regex, line)							# Finds relevant variables for parsing.
					if res:
						sp_code = res.group(1)
						sp_name = res.group(2)
						if sp_name not in species_list:
							species_list.append(sp_name)
						eugroup = codes[sp_code]
						fnames = eugroup.ljust(20) + sp_name
						no_hits_outputWrite = ean_output.write(f"{og}\t{fnames}\n")

ean_output.close()

output = open(query + "_refined_eg.txt", "a")

# Summary stats.
# Will be written out to "xxxxxx_refined_eg.txt'.
bac_prop = round(len(bac_list) / len(og_list) * 100, 2)
overall_prop = round(len(og_list) / len(preanno_full_list) * 100, 2)
stats = "__STATS__"

per_bac = "\nPercentage of bacterial-dominated OGs at " + str(cutoff) + " cutoff: " + str(bac_prop)
per_euk = "Percentage of Eukaryote/Archaeal OGs: " + str(100 - bac_prop)
per_overall = "Overall percentage of OGs with hits in eggNOG: " + str(overall_prop) + "\n"

total = "Total number of OGs in query: " + str(len(preanno_full_list))
tot_minus = "Total number of OGs after bacteria removed: " + str(len(preanno_full_list) - len(bac_list))
tot_euk = "Total number of OGs with significant non-bacterial hits: " + str(len(euk_arc_list))

print(per_bac)
print(per_euk)
print(per_overall)
print(total)
print(tot_minus)
print(tot_euk)

outputWrite = output.write(f"\n{stats}{per_bac}\n{per_euk}\n{per_overall}\n{total}\n{tot_minus}\n{tot_euk}")

output.close()
