def main():
    frac = input("Fraction: ")

    print(convert(frac))


def convert(fraction):
    x, y = fraction.split("/")

    try:
        x = int(x)
        y = int(y)
    except ValueError:
        raise ValueError

    if y == 0:
        raise ZeroDivisionError

    elif x > y:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
