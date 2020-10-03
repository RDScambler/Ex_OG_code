			# grep OGxxxxxxx Atwista_Telonemids_interpro.gff3 > OG_gff3_output.txt; grep -v MobiDBLite OG_gff3_output.txt > OG_gff3_output_minusMobi.txt;
			# grep -e match\$[0-9]*_[0-9]*_[0-9]* -e \>.*_OGxxxxxxx.fal -o OG_gff3_output_minusMobi.txt > match_ids.txt
			# Above grep can be used prior to running this code to parse the relevant matches and queries into match_ids.txt
			# Note MobiDBLite matches are removed wih -v MobiDBLite.
			# It is necessary to separate the main interpro and PANTHER analyses.
			# Otherwise, when searching over multiple .gff3 files match values of one analysis will also return the equivalent match in another.
			# Since the analyses were done separately, the same match values correspond to completely unrelated seqs.
			# Processing one analysis at a time therefore seems to be the most sensible solution.
import re
import sys
import subprocess
from Bio import SeqIO
from Bio.Align.Applications import MuscleCommandline
from Bio import AlignIO

# Configure taxa as necessary.
# Configure file as _interpro or _panther as necessary.
# UPDATE: file type (interpro or panther) is now configured via the command line as sys.argv[1].
taxa = "Atwista_Telonemids_"
file = taxa + sys.argv[1] + ".gff3"
records = SeqIO.parse(file, "fasta")
match_ids = []

# line variable must be assigned the strip method with "\n" for it to successfully remove the newline.
# Sidenote: I was convinced the conditional 'not in' was broken when I used line.strip within the append method.
# Eventually I realised that 'duplicates' were being compared to their counterparts that had the newline stripped.
# They would then appear identical in the finished list, but in fact were not equal while the conditional was comparing them.
with open("match_ids.txt") as f:
	for line in f:
		line = line.strip("\n")
		if line not in match_ids:
			match_ids.append(line)

# Seq objects are captured from original file using Bio.SeqIO.
# IDs from these are compared with the match IDs of interest.
# The query seqs starting with ">" must be removed in order to match with the Seq object IDs.
align_file = open("matches_to_align.fasta", "w")
for record in records:
	for match in match_ids:
		if match.startswith(">"):
			match = match.replace(">", "")
		if record.id == match:
			outputWrite = align_file.write(f"{'>'}{record.id}\n{record.seq}\n")

align_file.close()

# Seq file to be aligned does not seem to work whilst it is still open and/or is stored as a variable.
# May create issues with changing taxon names.
# Printing alignment is mostly pointless since it is far to large too display.
# Next step is to trim and reduce number of seqs aligned.
cline = MuscleCommandline(input="matches_to_align.fasta", out="align_output.txt", clw=True)
cline()
alignment = AlignIO.read("align_output.txt", "clustal")
print(alignment)


# I have realised the match seqs are in fact just snippets of the original queries, NOT ref motifs from the dbs.
# The alignment may still be useful however.
# The match seqs may need filtering so as to obtain a meaningful, readable alignment.
# One approach is to remove the MobiDBLite matches, which do not have meaningful annotations.
