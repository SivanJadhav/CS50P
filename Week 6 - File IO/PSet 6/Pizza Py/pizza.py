import sys
import csv
from tabulate import tabulate

# Only Accept One Command Line Argument
if len(sys.argv) > 2:
    sys.exit("Too many arguments!")
if len(sys.argv) < 2:
    sys.exit("Too few arguments!")

# Only Accept CSV File
if not sys.argv[1].endswith(".csv"):
    sys.exit("Not A CSV File")

# Assign Variables User Friendly Names
file_name = sys.argv[1]

# "Trying" to Open The File
try:
    with open(file_name, "r") as file:
        reader = csv.reader(file)

        print(tabulate(reader, headers="firstrow", tablefmt="grid"))


except FileNotFoundError:
    sys.exit("File not found!")
