import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")
#cereal_csv = os.path.join("/Users/schari/Desktop/LearnPython/03-Python/3/01-Evr_CerealCleaner/Resources", "cereal.csv")
# Open and read csv
with open(cereal_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    #csv_header = next(csvfile)
    #print(f"Header: {csv_header}")
    for row in csv_reader:
        if float(row[7]) >= 5:
            print(row)
