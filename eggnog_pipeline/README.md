### Eggnog Pipeline


This directory contains all python scripts associated with pre- and  
post-analysis of sequences using eggnog-mapper.  

**parse_file_eg.py**
All OG filenames present in all the outputs of a particular directory  
are parsed into one output file. These OG files may typically result  
from a find_group.py analysis, corresponding to a particular biological  
question.

**parse_seq.py**  
The output file from parse_file_eg.py is used to locate and parse all  
relevant sequence files in OG_arb-fal into another file ready for eggnog  
annotation. emapper.py can then be run from the command line in the  
eggnog-mapper directory.

**refine_and_parse_eg.py**
This is the main script used post-analysis to format eggnog output files.  
NOTE: not all information (GO, Kegg pathways) is parsed out so raw eggnog  
files should not be discarded. Key details are parsed out in a readable  
format. Any sequences that are not returned with a hit in the analysis are  
here also parsed into an output file. Finally, a contamination cutoff point  
is requested as an input, and OGs with proportions of top-hit bacterial  
sequences above and below that cutoff point are parsed into two separate 
output files.
NOTE: refine_and_parse_eg.py is currently configured with ventral groove  
inputs and outputs.
 
group.count_ogs() can be used to return a list of relevant OGs. This  
supersedes og_list.py (count_ogs() regex is more flexible).
