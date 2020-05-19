			# This script will refine and parse the raw output from interpro .tsv and .gff3 files.
			# Note that MobiDBLite entries are removed since these are not informative (at least not so far as I can tell).
			# Raw interpro output files should NOT be deleted, just in case.
			# Could look into a further output file that incorporated eggNOG AND interpro annotation?
import full_og_list
import re

# Configure taxa as necessary.
taxa = "Atwista_Telonemids"
og_list = full_og_list.full_og_list("/mnt/c/Users/scamb/Documents/uob_msc/Genome_data/OG_arb-fal/new_outputs/Atwista_Telonemids_output.txt")
tsv_output = taxa + "_interpro.tsv"
output = open(taxa + "_refined_interpro.tsv.txt", "w")

# Iterate over each og in order!
# Write out to a file in correct order.
# Remove MobiDB entries (not useful).
for og in og_list:
	with open(tsv_output) as f:
		for line in f:
			if "MobiDBLite" in line:
				pass
			else:
				spline = re.split("\t", line)
				id = spline[0]
				splid = re.split("_", id)
				specimen_id = splid[1]
				og_id = splid[3].rstrip(".fal\r")
				seq_length = spline[2].ljust(10)
				analysis = spline[3].ljust(20)
				accession = spline[4].ljust(20)
				description = spline[5]#
				start = spline[6]
				stop = spline[7]
				evalue = spline[8]
				if og in line:
					if len(spline) > 11:
						ipr_code = spline[11]
						annotation = spline[12]
						outputWrite = output.write(f"{og_id}\t{specimen_id}\t{seq_length}{analysis}{accession}{description}\t{start}\t{stop}\t{evalue}\t{ipr_code}\t{annotation}")
					else:
						outputWrite = output.write(f"{og_id}\t{specimen_id}\t{seq_length}{analysis}{accession}{description}\t{start}\t{stop}\t{evalue}\n")
	# Adds new line between OGs for clarity.
	outputWrite = output.write("\n")

output.close()

gff3_output = taxa + "_interpro.gff3"
output = open(taxa + "_refined_interpro.gff3.txt", "w")

# New formatted output is written for the .gff3 file.
for og in og_list:
	with open(gff3_output) as f:
		for line in f:
			if line.startswith(">"):
				break
			if "MobiDBLite" in line:
				pass
			elif line.startswith("#"):
				pass
			else:
				spline = re.split("\t", line)
				splid = re.split("_", spline[0])
				og_id = splid[3].rstrip(".fal\r")
				analysis = spline[1].ljust(20)
				start = spline[3]
				stop = spline[4]
				evalue = spline[5]
				attributes = spline[8]
				sig_desc = re.search(r"\w*;signature_desc=(.*)$", attributes)
				name = re.search(r"\w*;Name=(.*)$", attributes)
				if sig_desc:
					res = sig_desc.group(1)				# If signature description is present, this will be captured (along with remainder of line, inc. name).
				elif name:
					res = name.group(1)				# Otherwise name plus rest of line will be captured.
				else:
					res = " "					# If name not present, no other useful info is in attributes.
				if og in line:
					outputWrite = output.write(f"{og_id}\t{splid[1]}\t\t{analysis}{start}\t{stop}\t{evalue}\t{res}\n")

	outputWrite = output.write("\n")

output.close()
