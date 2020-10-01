### OG Results Pipeline

This directory contains all the scripts necessary to generate all the unique orthogroups shared by every pairwise  
eukaryote group in my dataset. The outputs are then calculated as a proportion of each group's genome. Outputs are  
converted into heatmaps using og_to_heatmap.py. Different subgroups can be analysed by invoking different code maps  
and group lists. Currently 12, 15, and 18-length group lists are present. These and their corresponding code maps  
can all be found in the group.py module, instantiated with OrthogroupSearch.

The main piece of code is find_group(), now integrated into group.py, though the actual script iterating over each 
pair of groups is find_group.py. setquery.py expands on this, taking input to customise searches.

**find_group.py**  
This iterates over every pairwise group of eukaryotes in the dataset and finds OGs that are unique for each pair of groups. 
The necessary code map is configured from the command line with sys.argv[1].

**total_genome.py**  
Similar to find_group.py, totalGenome.py finds all the OGs of each group in the dataset, but doesn't take exclusivity 
into account. The total genome is therefore parsed, and this is used to calculate the proportional data in 
table_pairwise_prop.py. Output files from totalGenome.py are stored in total_genome.

**group.py**  
This module contains key functions: parse_total() is a dictionary storing the results of total_genome.py (note total.py was also used 
previously as an intermediary - no longer necessary). codes(), alt_codes() and alt_codes_18() contain the different species code 
dictionaries, depending on which group sets are being considered. find_group() carries out the group search in OG_arb-fal.

**og_to_heatmap.py**  
This script integrates unique OG data extraction, proportion of genome calculation (optional) and conversion to a Matplotlib heatmap. 
Own group values are removed. The heatmap centrepoint is adjustable, drawing on the function defined in shift_colormap.py.

**setquery.py**  
This allows customisable searches for any number of eukaryote groups, using find_group().
