import re
import glob

to_parse = glob.glob('*.fal')

for file in to_parse:
	i = 0
	with open(file) as f:
		for line in f:
			i += 1
			m =  re.search(r'^[^>]\w*[_|0]', line)		# Checks for missing '>' in sp.code line
			if m:
				linecheck = 'Error: missing >, line ' + str(i) + ', file: ' + str(file)
				print(linecheck)
