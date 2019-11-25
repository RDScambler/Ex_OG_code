import glob
import re

j = 0
query = []
code_map = {}
group_names = []
nameError = "Incorrect name: please check spelling."
genome = open('C:\\Users\\scamb\\Documents\\UoB MSc\\Genome_data\\Group outputs\\genomeOutput.txt', 'w')

with open('Eukaryote_codes.txt') as f:
    for line in f:
        fields = re.split("\t", line.strip())
        code_map[fields[0]] = fields[1]
        if fields[1] not in group_names:
            group_names.append(fields[1])

while True:
	print('First group query:')                             #Requesting a group
	query1 = input()
	if query1 not in group_names:
		print(nameError)
	else:
		break

query.append(query1)

while True:
	print('Second group query (or enter to skip):')         #Allows second input to be optional
	query2 = input()
	if query2 == '':
                break
	elif query2 not in group_names:
		print(nameError)
	else:
		break

query.append(query2)

to_parse = glob.glob('*.fal')				#Searches through all .fal files.

for file in to_parse:
    groups_present = []
    with open(file) as f:
        for line in f:
            if line.startswith('>'):
                fields = re.split('_', line)            #Separates sp. code
                species_code = fields[0][1:]		# Removes '>'
                for i in code_map:                      #Linking sp. code to group
                    group = code_map[species_code]
                    if group not in groups_present:     #Adding to group array if new group
                        groups_present.append(group)
    if groups_present == query:                         #Adds file to output if it matches query
        genomewrite = genome.write(f'{file}\n')
        j += 1
    elif groups_present == query[::-1]:                 #Accounts for variation in the list order
        genomewrite = genome.write(f'{file}\n')
        j += 1

genomewrite = genome.write(f'Shared gene families: {j}')
genome.close()
