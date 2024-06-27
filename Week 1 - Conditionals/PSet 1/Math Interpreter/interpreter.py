question = input("Question: ").strip().split(" ")

x = int(question[0])
y = question[1]
z = int(question[2])

match y:
    case "+":
        print(float(x + z))
    case "-":
        print(float(x - z))
    case "*":
        print(float(x * z))
    case "/":
        print(float(x / z))
    case _:
        raise "No Operation"
