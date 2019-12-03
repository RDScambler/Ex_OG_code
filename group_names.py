import re				# *** groups() function is defined here. ***
import glob

to_parse = glob.glob("*.txt")


def groups():
	group_names = []
	code_map = {}
	with open('Eukaryote_codes.txt') as f:
		for line in f:
			fields = re.split("\t", line.strip())
			code_map[fields[0]] = fields[1]
			if fields[1] not in group_names:
				group_names.append(fields[1])
	return group_names

