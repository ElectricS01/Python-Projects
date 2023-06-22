num = input("Enter the number 1, 2, 3, or 4: ")
try:
    num = int(num)
except ValueError as e:
    num = "Invalid"

if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
elif num == 4:
    print("Four")
else:
    print("Invalid number")
