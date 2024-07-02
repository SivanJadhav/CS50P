def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    flt = float(d.removeprefix("$"))

    return flt


def percent_to_float(p):
    flt = float((p.removesuffix("%"))) / 100

    return flt


main()
