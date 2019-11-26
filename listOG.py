import re
import os
import glob

def groupname():
	"""This is a function asking the user for the name of a Eukaryote group as an input. The pre- and post-string additions are formatted to enable searches for relevant files in the directory."""
	global gname
	gname = "OG_"
	gname += input("Group name: \n")
	answer = input("Compare within own group or with other groups? (Reply Own or Others) \n")
	if answer == "Others":
		gname += "_*"
	else:
		gname += "_output.txt"

groupname()

print("Shared gene families: \n")
to_parse = glob.glob(gname)				# to_parse doesn't seem to work with single files, hence the if, else statements are used.

if gname.endswith("_*"):
	for file in to_parse:
		base = os.path.splitext(file)		# Splits the .ext from the filename.
		name = str.split(base[0], "_")		# Splits the filename by the "_" character.
		print(name[2],"\t", end="")		# Prints the name of the group to be compared with. For this reason it is important that the query group always be printed first in the filename.
		with open(file) as f:
			for line in f:
				a = re.search(r"Shared gene families:\s(\w*)", line) 	# Searches for the relevant string and corresponding figure (number of OGs).
				if a:
					print(a.group(1))

else:
	with open(gname) as f:		# This is used for 'Own' comparison, since only one file will (should) ever be returned.
		for line in f:
			b = re.search(r"Shared gene families:\s(\w*)", line)
			if b:
				print(b.group(1))
