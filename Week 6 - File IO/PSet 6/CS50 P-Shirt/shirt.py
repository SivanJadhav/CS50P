import sys
from PIL import Image, ImageOps

# Only Accepting Two Command Line Arguments
if len(sys.argv) > 3:
    sys.exit("Too many arguments!")
elif len(sys.argv) < 3:
    sys.exit("Too few arguments!")

# Only accepting image file types
if (
    not sys.argv[1].endswith(".png")
    and not sys.argv[1].endswith(".jpg")
    and not sys.argv[1].endswith(".jpeg")
):
    sys.exit("Only Image Files Are Accepted")

elif (
    not sys.argv[2].endswith(".png")
    and not sys.argv[2].endswith(".jpg")
    and not sys.argv[2].endswith(".jpeg")
):
    sys.exit("Only Image Files Are Accepted")

rem, extension1 = sys.argv[1].split(".")
rem, extension2 = sys.argv[2].split(".")

if extension1 != extension2:
    sys.exit("Both Files Should Have Same Extension")

# Doing the Photoshop
inpt = sys.argv[1]
outpt = sys.argv[2]

try:
    with Image.open(inpt) as image:
        shirt = Image.open("shirt.png")

        image = ImageOps.fit(image, size=(shirt.size), method=3, bleed=0)

        image.paste(shirt, mask=shirt)

        image.save(fp=outpt)
except FileNotFoundError:
    sys.exit("File Not Found!")
