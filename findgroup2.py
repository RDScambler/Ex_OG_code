
import glob
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
        for i in range(len(group_names)):                       # Iterates over every element of group_name by every other element
                query = group_names[j], group_names[i]
                file1 = '_'.join(query)				# Formats query for filenaming purposes
                file1 += '_output'
                if group_names[j] != group_names[i]:
                        group_set = set(query)                  # Creates set, disregarding the order.
                        x = 0					# x value necessary for the if else statement (lines 40-45).
                else:                                           # Modifies group_set if j == i to only have 1 element..
                        group_set = [group_names[j]]		# Creates array. Single element array will match with (unconverted) single element instances of groups_present.
                        x = 1
                if group_set not in all_sets:    		# Excludes sets which already exist.
                        all_sets.append(group_set)
                        filename = "%s.txt" % file1		# Formatting filename.
                        genome = open(filename, 'w')
                        to_parse = glob.glob('*.fal')		# Searches through all .fal files.
                        k = 0					# Counter (giving total exclusive OGs for set).
                        for file in to_parse:
                                groups_present = []
                                with open(file) as f:
                                        for line in f:
                                                if line.startswith('>'):
                                                        fields = re.split('_', line)            # Separates sp. code
                                                        species_code = fields[0][1:]		# Removes '>'
                                                        for i in code_map:                      # Linking sp. code to group
                                                                group = code_map[species_code]
                                                                if group not in groups_present:     	# Adding to group array if new group
                                                                        groups_present.append(group)
                                if x == 0:								# Converts array to set (so order is irrelevant).
                                        set_present = set(groups_present)
                                else:									# groups_present remains as array to match with single element instances of group_set.
                                        set_present = groups_present
                                if group_set == set_present:
                                        genomewrite = genome.write(f'{file}\n') 	# Adds file to output if it matches query
                                        k += 1
                        genomewrite = genome.write(f'Shared gene families: {k}')
                        genome.close()
