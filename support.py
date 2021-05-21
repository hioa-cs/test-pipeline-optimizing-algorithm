import csv


def get_dataset(file_name):
    with open('file_name', newline="\n") as csvfile:
        reader = csv.DictReader(csvfile,  delimiter=';')
        for row in reader:
            print(row)