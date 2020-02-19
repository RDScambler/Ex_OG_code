			# table6.py is again modified, this time to output totals/own OG data to R as a vector.
import re
import group
import glob

output = open("vector_totals_own.txt", "w")
correct_order_totals_own = ["SAR", "Other", "Haptista", "Archaeplastida", "Obazoa", "Discoba", "Ancyromonadida", "Cryptista", "Amoebozoa", "Metamonads", "Malawimonadidae"]

for eugroup in correct_order_totals_own:								# Choose list as appropriate.
	with open("group_totalvsEOGs.txt") as f:
		for line in f:
			if eugroup in line:
				res = re.split(r"\s+", line.strip())
				outputWrite = output.write(f"{res[2]} {res[1]} ")

output.close()
