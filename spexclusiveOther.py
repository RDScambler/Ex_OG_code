import re
import group

codes = group.codes()
othersp = []
output = open("sp_Other_exclusives.txt", "w")

for sp in codes:
	gr = codes[sp]
	if gr == "Other":
		othersp.append(sp)

freq = []

for species in othersp:
	i = 0
	with open("sp_Other.txt") as f:
		for line in f:
			res = re.split(r"\W+", line.strip())
			if species in res:
				if len(res) < 5:
					i += 1
					outputWrite = output.write(f"{res}\n")
	freq.append(i)

otherdic = dict(zip(othersp, freq))
print(otherdic)
outputWrite = output.write(str(otherdic))
