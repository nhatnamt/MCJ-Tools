import csv

with open('eBay.csv', mode='r') as csv_file:
    next(csv_file)
    csv_reader = csv.DictReader(csv_file,  delimiter=',',
                    skipinitialspace=True,
                    quoting=csv.QUOTE_ALL)
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        print(f'\t{row["name"]} works in the {row["department"]} department, and was born in {row["birthday month"]}.')
        line_count += 1
    print(f'Processed {line_count} lines.')
    t = input('rrr')