def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """Validates Plate Name"""

    # Must Contain At Least 2 Characters and 6 at Max. All of them should be letters and numbers
    if not (2 <= len(s) <= 6) or not s.isalnum():
        return False

    # Plate Should At Least Start With Two Letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    # Numbers can only be used at the end of the plate, and the first number should not be zero
    number_started = False
    for char in s:
        if char.isdigit():
            if not number_started:
                if char == "0":
                    return False
                number_started = True
        elif number_started:
            return False

    # Already satisfied that there are no periods, spaces, or punctuation marks
    # by the isalnum() check

    return True


main()
