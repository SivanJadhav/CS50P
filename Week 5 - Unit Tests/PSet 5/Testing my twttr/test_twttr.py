from twttr import shorten


def test_shorten():
    # Testing Without Capitalization
    assert shorten("this was cs50") == "ths ws cs50"

    # Testing With Capitalization
    assert shorten("THIs WaS cS50") == "THs WS cS50"

    # Testing With Capitalization and Punctuation Marks
    assert shorten("THIS, Was Cs50!") == "THS, Ws Cs50!"

    # Testing with numbers
    assert shorten("1234567890") == "1234567890"


if __name__ == "__main__":
    main()
