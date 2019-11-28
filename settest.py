import re

code_map = {}
group_names = []
all_sets = []

with open('Eukaryote_codes.txt') as f:
    for line in f:
        fields = re.split("\t", line.strip())
        code_map[fields[0]] = fields[1]
        if fields[1] not in group_names:
            group_names.append(fields[1])

for j in range(len(group_names)):
	for i in range(len(group_names)):			# Iterates over every element of group_name by every other element
		query = group_names[j], group_names[i]
		group_set = set(query)					# Converts list to set, disregarding the order.
		if group_set not in all_sets and len(group_set) > 1:	# Excludes single element sets and sets which already exist.
			all_sets.append(group_set)

print(all_sets)
