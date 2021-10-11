import csv


def write_csv_file(file, rows):
    with open(file, 'a', newline='') as file:
        writer = csv.writer(file)
        for row in rows:
            writer.writerow(row)
