			# This script will print out the groups present in certain OGs.
			# Is only a temporary script - just needed to see the constituent taxa of 'Other' in certain OGs.
			# The OGs in question are from 4-way ventral groove-bearing eukaryote sets.
import group
import re

vg = "setquery_outputs/ventral_groove/ventral_groove_minus_one.txt"
og_list = []
og_list = group.count_ogs(vg)

# Append str to og_list using list comprehension.
# Note: a for loop og + .fal will not keep the changes.
og_list = [og + ".fal" for og in og_list]
to_parse = og_list

code_map = group.alt_codes_18()

# Lifted from find_group.
for falfile in to_parse:
	groups_present = []
	with open(falfile) as f:
		for line in f:
			if line.startswith('>'):
				fields = re.split('_', line)                            # Separates sp. code
				species_code = fields[0][1:]                            # Removes '>'
				for i in code_map:                                      # Linking sp. code to group
					gr = code_map[species_code]
					if gr not in groups_present:               	# Adding to group array if new group
						groups_present.append(gr)
	print(falfile, groups_present)

