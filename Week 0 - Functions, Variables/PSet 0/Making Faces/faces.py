def main():
    string = input("Text: ")

    print(convert(string))


def convert(inpt):
    text = inpt.replace(":)", "🙂").replace(":(", "🙁")

    return text


main()
