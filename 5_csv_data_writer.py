import csv

with open('names.csv', 'w') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter="\t", quotechar="|")

    writer.writeheader()
    writer.writerow({'first_name': 'Javed', 'last_name': 'Mian\tdad'})
    writer.writerow({'first_name': 'Bilawal', 'last_name': 'Zardari'})
    writer.writerow({'first_name': 'Rohit', 'last_name': 'Sharma'})

with open('names.csv') as csvfile:
    fieldnames = ['first_name', 'last_name']
    reader = csv.DictReader(csvfile, fieldnames=fieldnames, delimiter="\t", quotechar="|")

    for row in reader:
        print(row['first_name'], ascii(row['last_name']))
