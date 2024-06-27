# Getting The Input
try:
    file_ex = input("File name: ").strip().lower().split(".")
    file_ex = file_ex[(len(file_ex) - 1)]
except IndexError:
    file_ex = None

# Determining Output

# Determining Images in General
image_exs = ["gif", "jpg", "jpeg", "png"]

if file_ex == "jpg" or file_ex == "jpeg":
    print("image/jpeg")

elif file_ex in image_exs:
    print(f"image/{file_ex}")

# Determining Other Types
elif file_ex == "pdf":
    print("application/pdf")

elif file_ex == "txt":
    print("text/plain")

elif file_ex == "zip":
    print("application/zip")

# Otherwise give default input
else:
    print("application/octet-stream")
