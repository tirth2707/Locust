import csv

class readCsv:

    def __init__(self, file):
        try:
            file = open(file)
        except FileNotFoundError:
            print("File not found")

        self.file = file
        self.reader = csv.DictReader(file)
