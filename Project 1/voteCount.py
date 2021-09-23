# filename = 2021-09-14_party distribution_1_st_2021.csv

def valgFunction(filename, numberOfParties):
    districts_list = {}
    with open(filename, 'r', encoding='utf-8') as partydistr_file:
        header = partydistr_file.readline().strip().split(';')

    # Fylkenavn = column 2, Partikode = column 7, Totale votes = 12
        for line in partydistr_file:
            _, _, _, _, _, _, partycode, _, prosentvisoppsl, _, _, totalvotes, _, _, _, _, _, _ = line.split(';')
            districts_list[partycode] = districts_list.get(partycode, 0) + int(totalvotes)
            districts_list[partycode] = districts_list.get(partycode, prosentvisoppsl) # Why doesn't it add it to the list?

    print(f'{header[6]:20s}{header[12]:30s}{header[8]:30s}')
    print(74 * '-')

    counter = 0
    for partycode, totalvotes in sorted(districts_list.items(), key=lambda s: s[1], reverse=True):
        print(f'{partycode:20s}{totalvotes:15d}')
        counter += 1
        if counter == numberOfParties:
            break
