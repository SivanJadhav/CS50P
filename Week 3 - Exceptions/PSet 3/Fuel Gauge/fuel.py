def main():
    fraction = input("Fraction: ")

    while "/" not in fraction:
        input("Fraction: ")

    x, y = fraction.split("/")

    while True:
        try:
            x = int(x)
            y = int(y)

            while x > y:
                x, y = input("Fraction: ").split("/")

            break
        except (ValueError, ZeroDivisionError):
            pass

    percentage = round((x / y) * 100)

    if percentage >= 99:
        print("F")
    elif percentage <= 1:
        print("E")
    else:
        print(f"{percentage}%")


main()
