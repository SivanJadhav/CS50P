months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


def is_valid_date(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if year < 1000:
        return False
    return True


def get_valid_date():
    while True:
        date = input("Date: ").strip()

        if "/" in date:
            date_parts = date.split("/")
            try:
                month = int(date_parts[0])
                day = int(date_parts[1])
                year = int(date_parts[2])
            except ValueError:
                continue
            if is_valid_date(month, day, year):
                return year, month, day
        elif "," in date:
            date_parts = date.split(" ")
            date_parts[1] = date_parts[1].replace(",", "")
            try:
                month = months.index(date_parts[0]) + 1
                day = int(date_parts[1])
                year = int(date_parts[2])
            except (ValueError, IndexError):
                continue
            if is_valid_date(month, day, year):
                return year, month, day


while True:
    year, month, day = get_valid_date()
    print(f"{year}-{month:02}-{day:02}")
    break
