INPUT = 'country_list.txt'
OUTPUT = 'clean_country_list.txt'

with open(INPUT) as infile:
    with open(OUTPUT, mode='w') as outfile:
        for line in infile.readlines():
            newline = line.strip(' -').lower()
            outfile.write(newline)