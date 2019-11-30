import glob
import re


to_parse = glob.glob("*.txt")
output = open("group_data.txt", "w")
groupname = "Group"
headers = output.write(f"{groupname.ljust(25)}{'Gene families'}\n")		# Formatted headers using .ljust (pads loose space up to the value of argument).

for file in to_parse:
	name = re.split("_", file)
	with open(file) as f:
		for line in f:
			og = re.search(r"\w*:\s(\w*)", line)
			if og:
				fname = name[0].ljust(25)			# Formats spacing as with the headers.
				outputWrite = output.write(f"{fname}{og.group(1)}\n")

output.close()
