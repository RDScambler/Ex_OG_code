import sp
import group
import re


to_search = ['SAR', 'Ancyromonadida', 'Discoba', 'Haptista', 'Obazoa']		# Groups with an interestingly high number(?) of exclusive OG matches with 'Other'.
output = open("Other_sp_freq_output.txt", "w")

for group in to_search:
	grouplist = ['Other']
	grouplist.append(group)
	filename = "sp_" + "_".join(grouplist)
	filename += ".txt"
	sp.sp_find(grouplist, filename)

	res = sp.sp_count("Other", filename)
	outputWrite = output.write(f"{group}\t{str(res)}\n")


output.close()
