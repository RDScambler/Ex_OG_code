import group			# *** setquery.py can be used to search presence of OGs for 3+ groups. This can be used to link OGs to particular character traits. ***

query = []
group_names = group.groups()

print("Enter eukaryote group names (press enter when done):")

while True:
	answer = input()
	if answer == '':
		break
	elif answer not in group_names:
		print("Incorrect name. Please check spelling.")
	else:
		query.append(answer)

groupset = set(query)
group.find_group(groupset)

