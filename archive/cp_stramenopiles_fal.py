from shutil import copy
import group

stram_ogs = "new_outputs/Stramenopiles_Stramenopiles_output.txt"
dir = "stramenopile_fal"
ogs = group.count_ogs(stram_ogs)

# Using copy (rather than copyfile), since 2nd arg can be a dir.
for og in ogs:
    og = og + ".fal"
    copy(og, dir)