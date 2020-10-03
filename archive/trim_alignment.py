			# This is a simple alignment trimmer. The alignment is trimmed from the first full column.
			# Must be noted, therefore, that it may not be suitable for some alignments.

import sys
sys.path.insert(0, "/mnt/c/Users/scamb/Documents/Programming/Biopython")
from Bio import AlignIO

# Usage: python scriptname.py alignment format
aln = AlignIO.read(sys.argv[1], sys.argv[2])

for col in range(aln.get_alignment_length()):
    if not "-" in aln[:, col]:
        position = col
        print("First full column is {}".format(col))
        break

AlignIO.write(aln[:, position:], "trimmed_alignment.txt", "clustal")
