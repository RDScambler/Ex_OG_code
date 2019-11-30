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
	for i in range(len(group_names)):			# Iterates over every element of group_name by every other element.
		query = group_names[j], group_names[i]
		x = '_'.join(query)				# Joins query into a single string for filenaming purposes.
		x += '_output'
		if group_names[j] != group_names[i]:
			group_set = set(query)			# Converts list to set, disregarding the order.
		else:						# Modifies group_set if j == i.
			group_set = group_names[j]
		if group_set not in all_sets:			# Excludes already-existing sets from further analysis.
			all_sets.append(group_set)
			print(x)

print(all_sets)



