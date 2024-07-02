def main():
    tweet = input("Input: ")

    print(f"Output: {shorten(tweet)}")


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    tweet = " "

    for char in word:
        if char.lower() in vowels:
            continue
        else:
            tweet = tweet + char

    return tweet.lstrip()


if __name__ == "__main__":
    main()
