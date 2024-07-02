from bank import value


def test_bank():
    # Testing Without Capitalization
    assert value("hello motto") == 0
    assert value("hi david") == 20

    # Testing With Capitalization
    assert value("HelLo Motto") == 0
    assert value("hI dAvId") == 20
    assert value("ThIS WAs cS") == 100

    # Testing With Capitalization and Punctuation Marks
    assert value("ThIS WAs cS!!!") == 100

    # Testing With Capitalization, Punctuation Marks and Numbers
    assert value("ThIS WAs cS50!!!") == 100


if __name__ == "__main__":
    main()
