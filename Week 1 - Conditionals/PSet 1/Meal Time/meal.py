def main():
    time = input("Time: ").strip().lower()

    if "a.m." in time:
        time = 12 - (time.split(" "))[0]
    if "p.m" in time:
        time = 12 + (time.split(" "))[0]

    formatted_time = convert(time)

    # Determining The Type of Meal To Eat
    if 7 <= formatted_time and formatted_time <= 8:
        print("breakfast time")
    elif 12 <= formatted_time and formatted_time <= 13:
        print("lunch time")
    elif 18 <= formatted_time and formatted_time <= 19:
        print("dinner time")


def convert(time):
    """Returns time in decimal format"""

    # Using time as hours and minutes
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    formatted_time = float(hours + (minutes / 60))

    return formatted_time


if __name__ == "__main__":
    main()
