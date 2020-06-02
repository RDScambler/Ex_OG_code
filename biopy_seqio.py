		# Trialling Biopython here before incorporating into align_matches.py

import sys
sys.path.insert(0, "/mnt/c/Users/scamb/Documents/Programming/Biopython")
from Bio import SeqIO

records = SeqIO.parse("Atwista_Telonemids_interpro.gff3", "fasta")
match_ids = []
with open("match_ids.txt") as f:
	for line in f:
		match_ids.append(line.strip())

for record in records:
	for match in match_ids:
		if match.startswith(">"):
			match = match.replace(">", "")
		if record.id == match:
			print(record.id)
			print(record.seq)

#for record in records:
#	print(record.id)
