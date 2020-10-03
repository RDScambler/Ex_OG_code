			# Script to find OGs that are common to all eukaryote groups.
			# Both 15- and 18-split lists are used.
			# Also searches for OGs present in all groups but one, identifying those that are near-universal.
import os
import glob
import group

# Two different group classifications are defined, to be iterated over.
groups_15 = group.alt_groups()
groups_18 = group.alt_groups_18()
lists = [groups_15, groups_18]

# Corresponding code_maps are defined.
codes_15 = group.alt_codes()
codes_18 = group.alt_codes_18()

# First finds OGs common to all groups, 15- and 18-split.
# Note: the find_group function produces a long and unwieldly filename for large sets.
group.find_group(groups_15, codes_15)
group.find_group(groups_18, codes_18)

# Iterating over each list in turn.
# .remove() is used to remove one group at a time from each search.
# This is to capture OGs that are almost universally present, i.e. in every group but one.
for groups in lists:
	if groups == groups_15:
		codes = codes_15
	else:
		codes = codes_18
	for g in groups:
		removed_groups = groups[:]
		removed_groups.remove(g)
		group.find_group(removed_groups, codes)

to_parse = glob.glob("*_output.txt")

# Filenames are renamed here after they've been created.
# This saves interfering with the code in find_group().
for file in to_parse:
	filename = file.split("_")
	if "common" in filename:
		pass
	if len(filename) == 15:
		for g in groups_15:
			if g not in filename:
				os.rename(file, r"minus_" + g + "_15_output.txt")

	elif len(filename) == 18:
		for g in groups_18:
			if g not in filename:
				os.rename(file, r"minus_" + g + "_18_output.txt")
