			# Script for improving the readability of eggnog output files.
			# In principle should be applicable to all outputs, providing sp labels are suffixed with "_OGxxxxxxx".
			# Important not to discard raw .emapper.annotations files since GOs, kegg etc. are not transferred.
			# Script also parses out all ogs that have no hits in eggnog to a separate file.
			# Script now also parses bacterial and non-bacterial OGs using a customisable cutoff point.
			# These different processes are incorporated here since they all make use of the same og_list.
import re
import group

output = open("ventral_groove_refined_eg.txt", "w")
no_hits_output = open("ventral_groove_no_hits_eg.txt", "w")

codes = group.codes()
og_list = []
preanno_full_list = []
species_list = []
sp_label_regex = "(\w{,8})_\w*[tn|gn]\d+_(\w+\-\w+)_(OG\d+)"					# Splits up the first entry of output file (these are not tab-separated).

with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/ventral_groove.txt") as f:
	for line in f:
		if line.startswith("OG"):
			og = line.rstrip("\.fal\n\r")
			preanno_full_list.append(og)


with open("ventral_groove_output_og.emapper.annotations") as f:					# Filename must be edited as necessary.
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
			tax_scope = tabline[17].ljust(20)
			text_description = tabline[-1]
			if og not in og_list:							# Appends ogs to og_list for the purposes of identifying new ogs and inserting \n accordingly.
				og_list.append(og)
				outputWrite = output.write("\n")
			outputWrite = output.write(f"{og}\t{fnames}{e}{ftax_hit}{tax_scope}{text_description}\n")

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
						no_hits_outputWrite = no_hits_output.write(f"{og}\t{fnames}\n")


output.close()
no_hits_output.close()

euk_arc_output = open("ventral_groove_euk_arc.txt", "w")
bac_output = open("ventral_groove_bac.txt", "w")

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

for og in og_list:
	j = 0
	tax_list = []
	while j < 2:														# While loop is necessary to iterate over the file twice.
		i = 0														# The first loop appends all taxa in og to tax_list.
		with open("ventral_groove_refined_eg.txt") as f:								# The second compares the frequency of Bacterial seqs to the cutoff.
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
							outputWrite = euk_arc_output.write(line)
				else:												# Otherwise they are written to the bacterial output file.
					for line in f:
						if og in line:
							outputWrite = bac_output.write(line)
		j += 1														# j ensures while loop occurs twice.

euk_arc_output.close()
bac_output.close()
