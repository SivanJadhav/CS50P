import sys
import csv

# Initializing List Of Dicts to Put Data
data = []

# Only Accept Two Command Line Arguments
if len(sys.argv) > 3:
    sys.exit("Too many arguments!")
elif len(sys.argv) < 3:
    sys.exit("Too few arguments!")

# Only Accepting CSV Files
elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
    sys.exit("Only CSV Files are Accepted")

# Initializing Variables With Friendly Names
inpt = sys.argv[1]
outpt = sys.argv[2]

# "Try" To Open The First File
try:
    with open(inpt, "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            last, first = row["name"].split(",")
            first = first.strip()
            last = last.strip()

            data.append({"first": first, "last": last, "house": row["house"]})

except FileNotFoundError:
    sys.exit("File Not Found")

# "Try" To Open The Second File
try:
    with open(outpt, "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first", "last", "house"])

        writer.writeheader()

        for row in data:
            writer.writerow(
                {"first": row["first"], "last": row["last"], "house": row["house"]}
            )

except FileNotFoundError:
    sys.exit("File Not Found")
