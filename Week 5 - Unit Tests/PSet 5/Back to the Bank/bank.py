def main():
    usr_input = input("Greeting: ").lower().replace('"', "").replace(" ", "")

    print(value(usr_input))


def value(greeting):
    # Formatting Greeting
    greeting = greeting.lower().replace('"', "").replace(" ", "")

    # If Starts with "hello", output $0
    if greeting.startswith("hello"):
        return 0

    # If starts with "h", but not "hello" output $20
    elif greeting.startswith("h"):
        return 20

    # Else output $100
    else:
        return 100


if __name__ == "__main__":
    main()
