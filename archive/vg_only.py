			# This script will parse OGs that are comprised entirely of ventral groove-bearing cells.
import re
import full_og_list

# og_list is imported - created in a separate file for reusability.
output = open("vg_only.txt", "w")
og_list = full_og_list.full_og_list()

# non_vg are those species that lack a ventral groove.
# (inlcuded up to this point since they belong to same groups as species that have vgs).
# Eukaryote hits and no hits have been entered into the same output file.
# They are partitioned, so I see no reason not to.
# sublist is created for the purposes of adding newlines between OGs.
non_vg = ['Telonema-spP1', 'Telonema-spP2', 'Telonema-subtile', 'Thecamonas-trahens', 'Euglena-gracilis', 'Bodo-saltans', 'Naegleria-gruberi', 'Diplonema-papillatum', 'Hemimastix-kukwesjijk']
to_parse = ["ventral_groove_euk_arc_70percent.txt", "ventral_groove_no_hits_eg.txt"]
sublist = []

for file in to_parse:
	for og in og_list:
		sp_list = []
		j = 0
		while j < 2:										# j while loop created (same as in refine_and_parse.py) to first fill the sp_list for each OG.
			with open(file) as f:								# After this the sp_list is compared with the 'outlist' of non-vg spp.
				if j < 1:								# line is written out only if there is no intersection.
					for line in f:
						if og in line:
							res = re.split(r"\s+", line, maxsplit=6)
							sp_name = res[2]
							sp_list.append(sp_name)
				else:
					for line in f:
						if sp_list == []:
							pass
						elif og in line:
							if not set(non_vg).intersection(sp_list):
								if og not in sublist:
									sublist.append(og)
									newline = output.write("\n")
								line.rstrip("\n\r")
								outputWrite = output.write(line)
				j += 1

output.close()
