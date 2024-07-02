from emoji import emojize

aliases = {":thumbsup:": ":thumbs_up:", ":earth_asia:": "🌏"}

text = input("Input: ")

for alias in aliases:
    if alias in text:
        text = text.replace(alias, aliases[alias])

print(f"Output: {emojize(text)}")
