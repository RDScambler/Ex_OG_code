				# This script can be adapted for different input files as needed.
				# Raw data is taken from genbank, so many proteins occur multiple times.
				# Appending to description_list ensures only one of each kind is added to records.
				# This then avoids running the same query multiple times when BLASTing.
from Bio import SeqIO

description_list = []
records = []

for seq_record in SeqIO.parse("Colponema_vietnamica.gp", "genbank"):
	if seq_record.annotations["organism"] == "Acavomonas peruviana":
		pass
	elif seq_record.description not in description_list:
		description_list.append(seq_record.description)
		records.append(seq_record)

# SeqIO doesn't work in the for loop (overwrites previous).
# Best to append a list of records.
# Output file can be file-formatted as desired.
SeqIO.write(records, "Colponema_vietnamica_filtered.fasta", "fasta")

