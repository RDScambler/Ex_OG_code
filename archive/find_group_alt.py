				# Alternative to the original find_group.py, iterates over the divided 'Other' subgroups.
				# New alt_codes() and alt_groups() created in group.py to accomodate this.
import re
import glob
import group

codes = group.alt_codes()
new_groups = ['Apusomonada', 'Atwista', 'Collodictyonids', 'Hemimastigophora', 'Telonemids']
all_groups = group.alt_groups()
sorted_all_groups = sorted(all_groups)
all_sets = []

for eugroup in new_groups:
	for ogroup in sorted_all_groups:
		query = [eugroup, ogroup]
		if eugroup != ogroup:
			group_set = set(query)
		else:
			group_set = eugroup
		if group_set not in all_sets:				# Appends to all sets to ensure no duplicate analyses.
			all_sets.append(group_set)
			if isinstance(group_set, set):
				group_set = sorted(group_set)		# Reverts data to a sorted list so that names are alphabetical.
			group.find_group(group_set, codes)		# 2nd argument of find_group() can now be configured depending on which code set is needed.



