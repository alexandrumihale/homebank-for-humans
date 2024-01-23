import csv

with open('ing.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    next(csv_reader)  # Skip header

    data = [line for line in csv_reader]  # Store data in a list

with open('output.csv', 'w', newline='') as output_file:
    fieldnames = ['Data', 'Tip Tranzactie', 'Debit', 'Credit']
    csv_writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter="\t")
    #csv_writer.writeheader()

    for line in data:  # Iterate over the stored data, not csv_reader
        non_empty_fields = [field.strip() for field in line if field.strip() != '']


        if len(line) >= 9 and line[0] != '' and 'Titular Cont' not in line[0]:
            row_dict = {
            'Data' : line[0],            
            'Tip Tranzactie': line[3],
            'Debit': line[6],
            'Credit': line[8]
            }
            csv_writer.writerow(row_dict)
        else:
            print('Skipping line')
