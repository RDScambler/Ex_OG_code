import spgr		# *** Iterates over each eukaryote group, finding each occurence of an OG with every other group then counting frequencies (i.e total but not exclusive no. of shared OGs). ***
import group

groups = group.groups()
output = open("gr_freq_output.txt", "w")

for g in groups:
	filename = "gr_" + g + ".txt"
	spgr.gr_find(g, filename)
	res = spgr.gr_count(filename)
	outputWrite = output.write(f"{g}\t{str(res)}\n")

output.close()
