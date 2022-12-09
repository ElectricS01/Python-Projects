print('Made by ElectricS01 electrics01.itch.io ')


# Do Not Redistribute without permission

while 0 < 1:

    case = str.casefold(input("Lower to Upper, Upper to Lower or Toggle case(U/L/T)"))
    text = input("Enter text ")

    if ("u" or "upper") in case:
        print(text.upper())

    if ("l" or "lower") in case:
        print(text.lower())

    if ("t" or "toggle") in case:
        print(text.swapcase())

    print()
    end = str.casefold(input("Again?(y/n) "))

    if ("n" or "no") in end:
        exit()

    print()
