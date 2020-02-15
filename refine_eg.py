			# Script for improving the readability of eggnog output files.
			# In principle should be applicable to all outputs, providing sp labels are suffixed with "_OGxxxxxxx".
			# Important not to discard raw .emapper.annotations files since GOs, kegg etc. are not transferred.
			# Script also parses out all ogs that have no hits in eggnog to a separate file.
import re
import group

output = open("ventral_groove_refined_eg.txt", "w")
no_hits_output = open("ventral_groove_no_hits_eg.txt", "w")

codes = group.codes()
og_list = []
preanno_full_list = []
sp_label_regex = "(\w{,8})_\w*[tn|gn]\d+_(\w+\-\w+)_(OG\d+)"					# Splits up the first entry of output file (these are not tab-separated).

with open("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/ventral_groove.txt") as f:
	for line in f:
		if line.startswith("OG"):
			og = line.rstrip("\.fal\n\r")
			preanno_full_list.append(og)


with open("ventral_groove_output_og.emapper.annotations") as f:					# Filename nust be edited as necessary.
	for line in f:
		res = re.search(sp_label_regex, line)
		if res:
			sp_code = res.group(1)
			sp_name = res.group(2)
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
						eugroup = codes[sp_code]
						fnames = eugroup.ljust(20) + sp_name
						no_hits_outputWrite = no_hits_output.write(f"{og}\t{fnames}\n")

output.close()
no_hits_output.close()
