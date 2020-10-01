				# This scrpit iterates over every pairwise group of eukaryotes and every individual group to search for unique OGs.
				# Eukaryote groups are defined based on the code map specified in sys.argv[1].
import glob
import group
import sys

# Customise code map and group list with sys.argv[1].
og = group.OrthogroupSearch(sys.argv[1])
all_groups = og.group_list()

# Sort groups alphabetically.
sorted_all_groups = sorted(all_groups)
all_sets = []

# Iterate over every pair of groups.
for eugroup in sorted_all_groups:
	for ogroup in sorted_all_groups:
		query = [eugroup, ogroup]
		if eugroup != ogroup:
			query = set(query)

		# In this case the individual group is queried.
		else:
			query = eugroup

		# Append to all sets to ensure no duplicate analyses.
		if query not in all_sets:
			all_sets.append(query)

			# Reverts data to a sorted list so that names are alphabetical.
			# Query must enter find_group as a list.
			if isinstance(query, set):
				query = sorted(query)
			og.find_group(query)

