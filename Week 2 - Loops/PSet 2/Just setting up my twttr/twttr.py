tweet = input("Input: ")

vowels = ["a", "e", "i", "o", "u"]

print("Output: ", end="")

for char in tweet:
    if char.lower() in vowels:
        continue
    else:
        print(char, end="")

print()
