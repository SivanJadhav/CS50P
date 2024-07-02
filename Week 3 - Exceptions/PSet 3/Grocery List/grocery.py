items = {}

while True:
    try:
        item = input().upper().strip()

        if item in items:
            items[item] = items[item] + 1

        else:
            items[item] = 1

    except EOFError:

        if len(items) > 0:
            print()

            sorted_items = sorted(items)

            for itme in sorted_items:
                print(f"{items[itme]} ", end="")
                print(itme)

            exit(0)
        else:
            exit(0)
