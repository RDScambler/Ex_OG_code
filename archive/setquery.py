			# *** setquery.py can be used to search presence of OGs for 3+ groups. This can be used to link OGs to particular character traits. ***
			# Now modified to enable the use of different sp. code dictionaries and group lists in analysis, determined by sys.argv[1] and sys.argv[2]..
import group
import sys

# sys.argv[1] must equal groups, alt_groups or alt_groups_18.
# sys.argv[2] must equal codes, alt_codes, or alt_codes_18.

# function_mappings and select_function() function are defined to map the sys.argvs from strings to actual functions.
# Comma-separated returns allow multiple returns from the same function (only just realised this).
function_mappings = {'groups':group.groups(), 'alt_groups':group.alt_groups(), 'alt_groups_18':group.alt_groups_18(), 'codes':group.codes(), 'alt_codes':group.alt_codes(), 'alt_codes_18':group.alt_codes_18()}

def select_function():
    while True:
        try:
            return function_mappings[sys.argv[1]], function_mappings[sys.argv[2]]
        except KeyError:
            print('Invalid function, try again.')

# select_function is called with the relevant group list and codes - these should correspond else the program may fail.
group_list, sp_codes = select_function()
query = []

print("Enter eukaryote group names (press enter when done):")

while True:
	answer = input()
	if answer == '':
		break
	elif answer not in group_list:
		print("Incorrect name. Please check spelling.")
	else:
		query.append(answer)


# Must not convert query into a set - this disrupts find_group function (data type should be list).
sorted_group = sorted(query)
group.find_group(sorted_group, sp_codes)

