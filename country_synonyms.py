FILE_NAME = 'country_synonyms.txt'

countries = {}

with open(FILE_NAME) as file:
    for line in file.readlines():
        words = line.split()
        countries[words[0]] = words
