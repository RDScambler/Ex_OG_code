import re		# *** finds OGs unique to DTSAR (like spexclusive but more specific). ***

outlist = ['AtwisOrt', 'DrotaCRt', 'RramoCRt', 'TtrahApg', 'AmaspApt', 'HkukwHmt', 'SmultHmt']		# Testing Telonemids
freq = []
output = open("setDTSAR.txt", "w")
i = 0

with open("setsp_Discoba_SAR_Other.txt") as f:
	for line in f:
		res = re.split(r"\W+", line.strip())
		if "Shared" in line:
			pass
		elif not set(outlist).intersection(res):
			print(res)
			outputWrite = output.write(f"{str(res)}\n")
			i += 1
	freq.append(i)

dtsar = "DTSAR: " + str(freq)
print(dtsar)
outputWrite = output.write(dtsar)
