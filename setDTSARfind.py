import sp		# *** spfindOther.py modified here to search the species of the D + SAR + Other set (here abbreviated DTSAR since specific aim is to search Telonemids within Other. ***
import group
import re

grouplist = ['Other', 'Discoba', 'SAR']
sp.sp_find(grouplist, "sp_Discoba_SAR_Other.txt")

#	res = sp.sp_count("Other", filename)
#	outputWrite = output.write(f"{group}\t{str(res)}\n")


output.close()
