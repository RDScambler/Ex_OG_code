import re

lines = open('OG0015727.fal').readlines()

for line in lines:
	m =  re.search(r'^[^>]\w*[_|0]', line)
	if m:
		print('Yes')
	else:
		print('No')

