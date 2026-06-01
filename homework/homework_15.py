with open('airport-codes_csv.csv', mode='r', encoding='utf-8') as file:
    header_line = file.readline()

    name_index = 2
    country_index = 5

    for line in file:
        parts = line.strip().split(';')

        if len(parts) > country_index and parts[country_index] == 'UA':
            print(parts[name_index])
