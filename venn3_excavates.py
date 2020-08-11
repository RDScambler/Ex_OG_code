			# This script creates a venn diagram specifically using the excavates' uniquely shared OG data.
			# As such, it is designed only with the excavate taxa in mind.
			# See venn3_euk_groups.py to visulaise whole-proteome data of other eukaryote groups.

from matplotlib_venn import venn3, venn3_circles, venn3_unweighted
from matplotlib import pyplot as plt

# Overall dimensions of the figure can be adjusted with figsize.
plt.figure(figsize=(7,4))

# the venn3 function takes a 7-element list of subset sizes corresponding to each section of the digram.
# _unweighted can be appended to the function to balance circle sizes regardless of subsets.
vd = venn3_unweighted(subsets = (249, 315, 45, 17, 3, 7, 0), set_labels = ('Metamonads', 'Discoba', 'Malawimonadidae'))

# Configure the fontsize of each label
for text in vd.set_labels:
	text.set_fontsize(9)

# Creates a circle object to customise the circles themselves.
circle = venn3_circles(subsets=(1, 1, 1, 1, 1, 1, 1), lw=1.0)

# Set the colour of each patch if desired.
vd.get_patch_by_id('100').set_color('firebrick')
vd.get_patch_by_id('010').set_color('chartreuse')
vd.get_patch_by_id('001').set_color('teal')

# Add pad arg to increase distance between title and figure.
plt.title("Uniquely shared excavate orthogroups", fontsize=12, pad=15.0)
plt.savefig("venn3_excavates.pdf")
