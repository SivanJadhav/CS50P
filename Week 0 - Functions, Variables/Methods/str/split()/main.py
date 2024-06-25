# Asks user for their name
name = input("What's your name? ").strip().title()

# Splits user's name into first name and last name
name = name.split(" ")

# Says hello to user
print(f"hello, {name[0]}")
