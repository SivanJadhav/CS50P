import inflect

p = inflect.engine()

# Creating a list to hold the names
names = []

# Getting The Input
while True:
    try:
        names.append(input("Name: "))
    except EOFError:
        print()
        break

# Joining names
joined_stuff = p.join(names)

# Printing EVERYTHING
print(f"Adieu, adieu, to {joined_stuff}")
