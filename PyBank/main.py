import csv
import os
Path_File = os.path.join("./PyBank/Resources","Budget_Data.csv")

with open(Path_File, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

        