### OG Results Pipeline

This directory contains all the scripts necessary to generate all the unique orthogroups shared by every pairwise eukaryote group  
in my dataset. The outputs are then calculated as a proportion of each group's genome. Outputs are stored as both vectors to be  
processed in R and written out to Excel. Different subgroups can be analysed by altering the group lists that are found in the  
different scripts. Currently 12, 15, and 18-length group lists are present. These, and their corresponding dictionaries, can all  
be found in the group module.

**find_group.py**  
This iterates over every pairwise group of eukaryotes in the dataset and finds OGs that are unique for each pair of groups. This  
is now stored in the group module, however, the original script remains here.

**find_group_alt.py**  
This functions like the original find_group.py, but iterates over the divided 'Other' subgroups rather than the original groups.

**find_group_alt_18**  
As with find_group_alt.py, this script iterates over the divided subgroups of SAR and Haptista (as well as 'Other').

**totalGenome.py**  
Similar to find_group.py, totalGenome.py finds all the OGs of each group in the dataset, but doesn't take exclusivity into account.  
The total genome is therefore parsed, and this is used to calculate the proportional data in table_pairwise_prop.py. Output files  
from totalGenome.py are stored in total_genome.

**total.py**  
Integrates the functionality of former scripts parseOG.py and table6.py. Totals for every group are written out to group_total.txt  
(this output is used by parse_total(), kept in the group module). The within-group output data in new_outputs are then extracted  
and written out as a vector, with the corresponding totals data, in order, to vector_totals_own_split_other.txt. Outputs can be  
configured as needed by editing the group list to be iterated over.

**group.py**  
This module contains key functions: parse_total() is a dictionary storing the results of totalGenome.py. codes(), alt_codes() and  
alt_codes_18() contain the different species code dictionaries, depending on which group sets are being considered. find_group()  
carries out the group search in OG_arb-fal.

**table_pairwise.py**
This replaces table4.py (removed to reduce confusion) - it parses all the pairwise group data with 'Other' divided into its subgroups.  
Can be reconfigured to parse groups of choice. Data are ordered, formatted and written out to ordered_vector_data_minusown_xx.txt.  
NOTE: table4.py data is stored in ordered_vector_data_minusown.txt. Code must be reconfigured in table_pairwise.py to reproduce  
original data. In reality it should only require the editing of the group_names list. 

**table_pairwise_prop.py**  
Formerly table2.py Works the same as table_pairwise.py but converts the data to the proportion of each group's genome. Output is stored  
in ordered_vector_propdata_xx.txt. NOTE: as with table_pairwise.py, to configure output the group_names and correct_order lists should  
be edited (remember these need to be the same length! As does n in chunks(l, n)). This script now also outputs proportional data to an  
Excel file - the same output file as for table_pairwise_xlout.py. 

**table_pairwise_xlout.py**  
This script writes out totals data to an Excel file, 'Pairwise_18.xlsx'. Note the equivalent output is parsed for proportional data,  
having been integrated into table_pairwise_prop.py. 

**tabledic.py**  
Non-essential script but outputs proportional data (in prop_data.txt) in a nice dictionary format.

NOTE: other table.py scripts exist, due to various formatting approaches. These are now archived.
