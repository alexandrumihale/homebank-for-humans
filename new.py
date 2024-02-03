import csv

file = "ing.csv"
rows = []
fields = []

with open(file, "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    for row in csvreader:
        rows.append(row)
        for field in row:
            fields.append(field)






finalrows = "\n".join(map(str, rows))
excludingline = "Titular cont:"
#print(finalrows)

headers = ["Data", "Tip Tranzactie", "Debit", "Credit", "Ordonator", "Terminal"]

# Iterate through the list to merge with the previous list if the first element is empty
del rows[:2]
del rows[-10:]

merged_rows = [rows[0]]


for row in rows[1:]:
    if row[0] == "":
        # Merge with the previous row
        merged_rows[-1].extend(row[1:])
    else:
        # Add the row to the result
        merged_rows.append(row)


#print(merged_rows, sep="\n")

with open("output.csv", "w+", newline="\n") as output:
    output = csv.DictWriter(output, fieldnames=headers)
    output.writeheader()
    #output.writerows(merged_rows)

    for i in merged_rows:
        if all(excludingline not in i for i in i) and len(i) >= 21:
            details = {
            'Data' : i[0],            
            'Tip Tranzactie': i[3],
            'Debit': i[6],
            'Credit': i[8],
            'Ordonator': i[12],
            'Terminal': i[21]

            }
            output.writerow(details)



