import csv, sys

filename = "nums.txt"
with open(filename) as f:
    reader = csv.reader(f, delimiter=",", quotechar="|")
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit("file {}, line {}: {}".format(filename, reader.line_num, e))


with open('nums.txt', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['x'], row['z'])
